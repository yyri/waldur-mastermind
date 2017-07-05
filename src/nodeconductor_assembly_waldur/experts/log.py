from nodeconductor.logging.loggers import EventLogger, event_logger

from . import models


class ExpertRequestEventLogger(EventLogger):
    expert_request = models.ExpertRequest

    class Meta:
        event_types = ('expert_request_created',)
        event_groups = {
            'experts': event_types,
        }


event_logger.register('waldur_expert_request', ExpertRequestEventLogger)
