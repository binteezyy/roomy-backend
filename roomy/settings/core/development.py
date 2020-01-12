from .base import *
import os

ALLOWED_HOSTS = ['*', ]

INTERNAL_IPS = [
    '*',
    '192.168.1.14'
]
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
    }
#    'mysql': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'roomy-test',
#        'USER': config('DB_USERNAME'),
#        'PASSWORD': config('DB_PASSWORD'),
#        'HOST': config('DB_HOST'),   # Or an IP Address that your DB is hosted on
#        'PORT': config('DB_PORT'),
#    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

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

ROOT_URLCONF = 'apps.core.roomy_admin.urls'
