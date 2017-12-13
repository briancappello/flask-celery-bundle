from .flask_celery import FlaskCelery


celery = FlaskCelery()


EXTENSIONS = {
    'celery': celery,
}
