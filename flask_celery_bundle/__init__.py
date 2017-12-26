from flask_unchained import Bundle

from .extension import celery


class FlaskCeleryBundle(Bundle):
    command_group_names = ['celery']
    extensions_module_name = 'extension'
