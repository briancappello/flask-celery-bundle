from flask import current_app

from .extensions import celery

try:
    from flask_mail_bundle import mail
    from flask_mail_bundle.utils import make_message
except ImportError:
    # redefine the @celery.task decorator so we don't register a mail task when
    # the mail bundle isn't installed
    class celery:
        @staticmethod
        def task(*args, **kwargs):
            return lambda fn: None


def _send_mail_async(subject_or_message=None, to=None, template=None, **kwargs):
    subject_or_message = subject_or_message or kwargs.pop('subject')
    if current_app and current_app.testing:
        return async_mail_task.apply([subject_or_message, to, template], kwargs)
    return async_mail_task.delay(subject_or_message, to, template, **kwargs)


@celery.task(serializer='pickle')
def async_mail_task(subject_or_message, to=None, template=None, **kwargs):
    to = to or kwargs.pop('recipients', [])
    msg = make_message(subject_or_message, to, template, **kwargs)
    with mail.connect() as connection:
        connection.send(msg)
