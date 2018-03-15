import os


class BaseConfig:
    CELERY_BROKER_URL = 'redis://{host}:{port}/0'.format(
        host=os.getenv('FLASK_REDIS_HOST', '127.0.0.1'),
        port=os.getenv('FLASK_REDIS_PORT', 6379),
    )
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ('json', 'pickle')


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    pass
