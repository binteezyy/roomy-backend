import os
from .manifest import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


GLOBAL_APPS = [
    'apps.client.apps.ClientConfig',
    'apps.core.roomy_admin',
    'apps.core.roomy_core',
    'django_user_agents',
    'corsheaders',
]

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
