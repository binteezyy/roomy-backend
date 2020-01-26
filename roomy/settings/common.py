import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

GLOBAL_APPS = [
    'apps.client.apps.ClientConfig',
    'apps.core.roomy_admin',
    'apps.core.roomy_core',
]
