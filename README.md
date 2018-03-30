# Flask Celery Bundle

Adds Celery support to Flask Unchained projects


# Install

Install from PyPI:

```bash
$ pip install flask_celery_bundle
```

Add it to `unchained_config.BUNDLES`:

```python
# your_app_package/unchained_config.py

BUNDLES = [
    'flask_mail_bundle',
    'flask_celery_bundle',
    # ...
]
```

NOTE: If you're using `flask_mail_bundle`, then `flask_celery_bundle` must be listed *after* `flask_mail_bundle`.

# Configure

This package is just a tiny wrapper that integrates Celery with Flask, so it accepts all of the standard [celery configuration options](http://docs.celeryproject.org/en/latest/userguide/configuration.html). The only restriction is that, for compatibility with Flask, you must use the "old" uppercase setting names.

The default configuration included with this bundle uses `redis` as a message broker:

```python
import os

class BaseConfig:
    CELERY_BROKER_URL = 'redis://{host}:{port}/0'.format(
        host=os.getenv('FLASK_REDIS_HOST', '127.0.0.1'),
        port=os.getenv('FLASK_REDIS_PORT', 6379),
    )
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ('json', 'pickle')
```
