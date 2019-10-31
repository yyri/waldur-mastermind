# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-10 11:05
from decimal import Decimal
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators
import waldur_core.structure.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_squashed_0054'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('file', models.FileField(upload_to='support_attachments')),
                ('backend_id', models.CharField(max_length=255, unique=True)),
                ('mime_type', models.CharField(blank=True, max_length=100, verbose_name='MIME type')),
                ('file_size', models.PositiveIntegerField(blank=True, null=True, verbose_name='Filesize, B')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='support_attachments_thumbnails')),
            ],
            options={
                'abstract': False,
            },
            bases=(waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('backend_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IgnoredIssueStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                ('state', django_fsm.FSMIntegerField(choices=[(5, 'Creation Scheduled'), (6, 'Creating'), (1, 'Update Scheduled'), (2, 'Updating'), (7, 'Deletion Scheduled'), (8, 'Deleting'), (3, 'OK'), (4, 'Erred')], default=5)),
                ('backend_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('key', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, help_text='Link to issue in support system.', max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('impact', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('resolution', models.CharField(blank=True, max_length=255)),
                ('priority', models.CharField(blank=True, max_length=255)),
                ('resource_object_id', models.PositiveIntegerField(null=True)),
                ('first_response_sla', models.DateTimeField(blank=True, null=True)),
                ('resolution_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(waldur_core.structure.models.StructureLoggableMixin, waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IssueStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Status name in Jira.', max_length=255, unique=True)),
                ('type', django_fsm.FSMIntegerField(choices=[(0, 'Resolved'), (1, 'Canceled')], default=0)),
            ],
            options={
                'verbose_name': 'Issue status',
                'verbose_name_plural': 'Issue statuses',
            },
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('unit_price', models.DecimalField(decimal_places=7, default=0, max_digits=22, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('unit', models.CharField(choices=[('month', 'Per month'), ('half_month', 'Per half month'), ('day', 'Per day'), ('hour', 'Per hour'), ('quantity', 'Quantity')], default='day', max_length=30)),
                ('product_code', models.CharField(blank=True, max_length=30)),
                ('article_code', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(choices=[('requested', 'Requested'), ('ok', 'OK'), ('terminated', 'Terminated')], default='requested', max_length=30)),
                ('report', waldur_core.core.fields.JSONField(blank=True)),
                ('terminated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='support.Issue')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
            bases=(waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OfferingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('unit_price', models.DecimalField(decimal_places=7, default=0, max_digits=22, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('unit', models.CharField(choices=[('month', 'Per month'), ('half_month', 'Per half month'), ('day', 'Per day'), ('hour', 'Per hour'), ('quantity', 'Quantity')], default='day', max_length=30)),
                ('product_code', models.CharField(blank=True, max_length=30)),
                ('article_code', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfferingTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('config', django.contrib.postgres.fields.jsonb.JSONField()),
                ('sort_order', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'ordering': ['sort_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('icon_url', models.URLField(blank=True, verbose_name='icon url')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
            },
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.IntegerField(unique=True)),
                ('issue_type_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupportCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_id', models.CharField(max_length=255, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('native_name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField()),
                ('native_description', models.TextField(blank=True)),
                ('issue_type', models.CharField(choices=[('INFORMATIONAL', 'Informational'), ('SERVICE_REQUEST', 'Service request'), ('CHANGE_REQUEST', 'Change request'), ('INCIDENT', 'Incident')], default='INFORMATIONAL', max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('file', models.FileField(upload_to='support_template_attachments')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='support.Template')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateStatusNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, unique=True, validators=[waldur_core.core.validators.validate_name])),
                ('html', models.TextField(validators=[waldur_core.core.validators.validate_name])),
                ('text', models.TextField(validators=[waldur_core.core.validators.validate_name])),
                ('subject', models.CharField(max_length=255, validators=[waldur_core.core.validators.validate_name])),
            ],
        ),
        migrations.AddField(
            model_name='offeringplan',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='support.OfferingTemplate'),
        ),
        migrations.AddField(
            model_name='offering',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='support.OfferingPlan'),
        ),
        migrations.AddField(
            model_name='offering',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='structure.Project'),
        ),
        migrations.AddField(
            model_name='offering',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='support.OfferingTemplate'),
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, help_text='Help desk user who will implement the issue', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='support.SupportUser'),
        ),
        migrations.AddField(
            model_name='issue',
            name='caller',
            field=models.ForeignKey(help_text='Waldur user who has reported the issue.', on_delete=django.db.models.deletion.PROTECT, related_name='created_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='structure.Customer', verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='structure.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='reporter',
            field=models.ForeignKey(blank=True, help_text='Help desk user who have created the issue that is reported by caller.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reported_issues', to='support.SupportUser'),
        ),
        migrations.AddField(
            model_name='issue',
            name='resource_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='issue',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issues', to='support.Template'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='support.SupportUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='support.Issue'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='support.SupportUser'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='support.Issue'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('backend_id', 'issue')]),
        ),
    ]
