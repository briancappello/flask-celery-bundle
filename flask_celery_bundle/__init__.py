"""
    flask_celery_bundle
    ~~~~~~~~~~~~~~~

    Adds Celery support to Flask Unchained

    :copyright: Copyright © 2018 Brian Cappello
    :license: MIT, see LICENSE for more details
"""

__version__ = '0.1.0'


from flask_unchained import Bundle

from .extensions import celery


class FlaskCeleryBundle(Bundle):
    command_group_names = ['celery']
