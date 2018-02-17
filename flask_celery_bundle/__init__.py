from flask_unchained import Bundle

from .extensions import celery


class FlaskCeleryBundle(Bundle):
    command_group_names = ['celery']
