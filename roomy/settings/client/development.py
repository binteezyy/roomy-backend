from .base import *
from decouple import config
import os

ALLOWED_HOSTS = ['*']
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

print("\n\nBASE:",BASE_DIR)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
    }
}

# DEBUG TOOLBAR
INTERNAL_IPS = ['127.0.0.1',]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATIC_ROOT = '/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/media'
MEDIA_URL = '/media/'
