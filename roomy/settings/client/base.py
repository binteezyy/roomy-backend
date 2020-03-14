from decouple import config
from ..common import *
import os

STATIC_ROOT = os.path.join(BASE_DIR, '../apps/client/static/')

SECRET_KEY = config('SECRET_KEY')
RECAPTCHA_KEY = config('RECAPTCHA_KEY')
ROOT_URLCONF = 'config.client.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'webpush',
    'channels',
    'rest_framework',
    'sslserver',
    'social_django',
    'bootstrap_modal_forms',
    'sekizai',
    'numbers',
    # APPS
] + GLOBAL_APPS

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'apps/client/static/js/service_worker.js')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '799962262985-1bco370hresk0df19akuo4bmi02or742.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'KZ6ztb5sc_iaGrbKtrSvASTd'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "https://roomy.jjspscl.com",
    "https://storage.googleapis.com"
]

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

# https://web-push-codelab.glitch.me/
WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": config('WEBPUSH_PUBLIC_KEY'),
   "VAPID_PRIVATE_KEY": config('WEBPUSH_PRIVATE_KEY'),
   "VAPID_ADMIN_EMAIL": config('WEBPUSH_ADMIN_EMAIL')
}

WSGI_APPLICATION = 'config.client.wsgi.application'
ASGI_APPLICATION = 'config.client.asgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.media',
            ],
        },
    },
]


LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
PHONENUMBER_DEFAULT_FORMAT = "E164"
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config('SERVICE_EMAIL')
EMAIL_HOST_PASSWORD = config('SERVICE_EMAIL_PASSWORD')
