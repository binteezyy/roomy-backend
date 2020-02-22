import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

GLOBAL_APPS = [
    'apps.client.apps.ClientConfig',
    'apps.core.roomy_admin',
    'apps.core.roomy_core',
    'django_user_agents',
]

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
