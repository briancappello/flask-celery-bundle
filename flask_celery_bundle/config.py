import os

from .tasks import _send_mail_task


class BaseConfig:
    CELERY_BROKER_URL = 'redis://{host}:{port}/0'.format(
        host=os.getenv('FLASK_REDIS_HOST', '127.0.0.1'),
        port=os.getenv('FLASK_REDIS_PORT', 6379),
    )
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ('json', 'pickle')

    # configure flask_mail_bundle to send emails via celery
    MAIL_SEND_TASK = _send_mail_task
