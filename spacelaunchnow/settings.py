"""
Django settings for spacelaunchnow project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from spacelaunchnow import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.keys['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '.calebjones.me', '159.203.85.8', '.spacelaunchnow.me', '127.0.0.1', 'spacelaunchnow.me']
REST_FRAMEWORK = {
    'PAGE_SIZE': 1000,
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'drf_toolbox.serializers.ModelSerializer',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    )
}

LOGIN_REDIRECT_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] - [%(name)s - %(module)s - %(lineno)s] - %(message)s',
            'datefmt': '%m-%d-%Y %H:%M:%S'
        },
    },
    'handlers': {
        'django_default': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/django.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'digest': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/bot/daily_digest.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5
        },
        'notifications': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/bot/notification.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django_default', 'console'],
            'propagate': True,
        },
        'bot.digest': {
            'handlers': ['django_default', 'digest', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'bot.notifications': {
            'handlers': ['django_default', 'notifications', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.apps.ApiConfig',
    'rest_framework_docs',
    'bot',
    'djcelery',
    'embed_video',
    'jet',
    'django.contrib.admin',
    'django_user_agents',
    'django_filters',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spacelaunchnow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'spacelaunchnow.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# CELERY STUFF
BROKER_URL = "amqp://spacelaunchnow:spacelaunchnow@localhost:5672/vhost_spacelaunchnow"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = None

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'Webmaster <webmaster@spacelaunchnow.me>'
