from __future__ import unicode_literals

import logging
import six

from celery import shared_task
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse

from waldur_core.core import tasks as core_tasks
from waldur_core.structure.signals import resource_imported
from waldur_mastermind.common import utils as common_utils
from waldur_openstack.openstack_tenant import models as openstack_tenant_models
from waldur_openstack.openstack_tenant.views import InstanceViewSet

from . import models, exceptions, signals

logger = logging.getLogger(__name__)


class CreateNodeTask(core_tasks.Task):
    def execute(self, instance, user_id):
        node = instance
        content_type = ContentType.objects.get_for_model(openstack_tenant_models.Instance)
        flavor = node.initial_data['flavor']
        storage = node.initial_data['storage']
        image = node.initial_data['image']
        subnet = node.initial_data['subnet']
        group = node.initial_data['group']
        tenant_spl = node.initial_data['tenant_service_project_link']
        user = auth.get_user_model().objects.get(pk=user_id)

        roles_command = []

        if node.controlplane_role:
            roles_command.append('--controlplane')

        if node.etcd_role:
            roles_command.append('--etcd')

        if node.worker_role:
            roles_command.append('--worker')

        node_command = node.cluster.node_command + ' ' + ' '.join(roles_command)

        post_data = {
            'name': node.name,
            'flavor': reverse('openstacktenant-flavor-detail', kwargs={'uuid': flavor}),
            'image': reverse('openstacktenant-image-detail', kwargs={'uuid': image}),
            'service_project_link': reverse('openstacktenant-spl-detail', kwargs={'pk': tenant_spl}),
            'system_volume_size': storage,
            'security_groups': [{'url': reverse('openstacktenant-sgp-detail', kwargs={'uuid': group})}],
            'internal_ips_set': [
                {
                    'subnet': reverse('openstacktenant-subnet-detail', kwargs={'uuid': subnet})
                }
            ],
            'user_data': settings.WALDUR_RANCHER['RANCHER_NODE_CLOUD_INIT_TEMPLATE'].format(command=node_command)
        }
        view = InstanceViewSet.as_view({'post': 'create'})
        response = common_utils.create_request(view, user, post_data)

        if response.status_code != status.HTTP_201_CREATED:
            six.reraise(exceptions.RancherException, response.data)

        instance_uuid = response.data['uuid']
        instance = openstack_tenant_models.Instance.objects.get(uuid=instance_uuid)
        node.content_type = content_type
        node.object_id = instance.id
        node.content_type = content_type
        node.state = models.Node.States.CREATING
        node.save()

        resource_imported.send(
            sender=instance.__class__,
            instance=instance,
        )

    @classmethod
    def get_description(cls, instance, *args, **kwargs):
        return 'Create nodes for k8s cluster "%s".' % instance


@shared_task
def update_node(cluster_id):
    cluster = models.Cluster.objects.get(id=cluster_id)
    backend = cluster.get_backend()

    if cluster.node_set.filter(backend_id='').exists():
        backend_nodes = backend.get_cluster_nodes(cluster.backend_id)

        for backend_node in backend_nodes:
            if cluster.node_set.filter(name=backend_node['name']).exists():
                node = cluster.node_set.get(name=backend_node['name'])
                node.backend_id = backend_node['backend_id']
                node.save()

    has_changes = False

    for node in cluster.node_set.exclude(backend_id=''):
        if backend.node_is_active(node.backend_id):
            if node.state != models.Node.States.OK:
                node.state = models.Node.States.OK
                node.save(update_fields=['state'])
                has_changes = True
        elif node.state == models.Node.States.OK:
            node.state = models.Node.States.ERRED
            node.save(update_fields=['state'])
            has_changes = True
        else:
            pass

    if has_changes:
        signals.node_states_have_been_updated.send(
            sender=models.Cluster,
            instance=cluster,
        )


@shared_task(name='waldur_rancher.update_node_states')
def update_node_states():
    for cluster in models.Cluster.objects.exclude(backend_id=''):
        update_node.delay(cluster.id)
