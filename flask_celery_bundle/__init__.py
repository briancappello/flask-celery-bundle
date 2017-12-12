from flask_application_factory import Bundle

from .extension import celery


class FlaskCeleryBundle(Bundle):
    module_name = __name__
    command_group_names = ['celery']
    extensions_module_name = 'extension'
