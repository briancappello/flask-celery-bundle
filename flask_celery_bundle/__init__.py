from flask_unchained import Bundle

from .extension import celery


class FlaskCeleryBundle(Bundle):
    name = 'celery'
    extensions_module_name = 'extension'
