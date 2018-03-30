from flask import current_app

from .extensions import celery

try:
    from flask_mail_bundle import make_message, mail
except ImportError:
    # redefine the @celery.task decorator so we don't register a task when the
    # mail bundle isn't installed
    class celery:
        @staticmethod
        def task(*args, **kwargs):
            return lambda fn: None


def _send_mail_task(subject_or_message, to=None, template=None, **kwargs):
    if current_app and current_app.testing:
        return send_mail_async.apply([subject_or_message, to, template], kwargs)
    return send_mail_async.delay(subject_or_message, to, template, **kwargs)


@celery.task(serializer='pickle')
def send_mail_async(subject_or_message, to=None, template=None, **kwargs):
    to = to or kwargs.pop('recipients', [])
    msg = make_message(subject_or_message, to, template, **kwargs)
    with mail.connect() as connection:
        connection.send(msg)
