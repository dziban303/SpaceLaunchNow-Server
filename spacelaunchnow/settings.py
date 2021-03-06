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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = ['localhost', '.calebjones.me', '159.203.85.8', '.spacelaunchnow.me', '127.0.0.1', 'spacelaunchnow.me']
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'spacelaunchnow.pagination.SLNLimitOffsetPagination',
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'drf_toolbox.serializers.ModelSerializer',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/sec',
        'user': '200/sec'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
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
            'filename': 'log/daily_digest.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5
        },
        'notifications': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/notification.log',
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
    'django.contrib.sites',
    'rest_framework',
    'api.apps.ApiConfig',
    'rest_framework_docs',
    'bot',
    'djcelery',
    'embed_video',
    'material',
    'material.admin',
    'django.contrib.admin',
    'django_user_agents',
    'django_filters',
    'rest_framework.authtoken',
    'storages',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
    'collectfast',
# 'silk'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

GEOIP_DATABASE = 'GeoLiteCity.dat'
GEOIPV6_DATABASE = 'GeoLiteCityv6.dat'

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
                'spacelaunchnow.context_processor.ga_tracking_id',
                'spacelaunchnow.context_processor.use_google_analytics',
                'zinnia.context_processors.version',  # Optional
            ],
        },
    },
]

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
    ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('zinnia/fullwidth_entry_detail.html', 'Fullwidth template'),
]

USE_GA = not config.DEBUG

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

ZINNIA_MARKUP_LANGUAGE = 'markdown'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GA_TRACKING_ID = config.GOOGLE_ANALYTICS_TRACKING_ID

# CELERY STUFF
BROKER_URL = config.BROKER_URL
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
EMAIL_HOST = config.EMAIL_HOST
EMAIL_PORT = config.EMAIL_PORT
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = config.EMAIL_HOST_TLS
DEFAULT_FROM_EMAIL = config.EMAIL_FROM_EMAIL

# AWS Storage Information

AWS_STORAGE_BUCKET_NAME = config.STORAGE_BUCKET_NAME

# Not using CloudFront?
# S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# Using CloudFront?
# S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN
AWS_S3_CUSTOM_DOMAIN = config.S3_CUSTOM_DOMAIN

# Static URL always ends in /
STATIC_URL = config.S3_CUSTOM_DOMAIN + "/"

# If not using CloudFront, leave None in config.
CLOUDFRONT_DOMAIN = config.CLOUDFRONT_DOMAIN
CLOUDFRONT_ID = config.CLOUDFRONT_ID

AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY

AWS_LOCATION = 'static'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',

}

STATIC_URL_AWS = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

MEDIA_LOCATION = 'media'
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
STATICFILES_DIRS = [os.path.join(PROJECT_PATH, 'static')]
STATICFILES_LOCATION = 'static/home'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
AWS_PRELOAD_METADATA = True

LOGO_LOCATION = MEDIA_LOCATION + '/logo'  # type: str
LOGO_STORAGE = 'custom_storages.LogoStorage'

DEFAULT_LOCATION = MEDIA_LOCATION + '/default'  # type: str
DEFAULT_STORAGE = 'custom_storages.DefaultStorage'

AGENCY_IMAGE_LOCATION = MEDIA_LOCATION + '/agency_images'  # type: str
AGENCY_IMAGE_STORAGE = 'custom_storages.AgencyImageStorage'

AGENCY_NATION_LOCATION = MEDIA_LOCATION + '/agency_nation'  # type: str
AGENCY_NATION_STORAGE = 'custom_storages.AgencyNationStorage'

ORBITER_IMAGE_LOCATION = MEDIA_LOCATION + '/orbiter_images'  # type: str
ORBITER_IMAGE_STORAGE = 'custom_storages.OrbiterImageStorage'

LAUNCHER_IMAGE_LOCATION = MEDIA_LOCATION + '/launcher_images'  # type: str
LAUNCHER_IMAGE_STORAGE = 'custom_storages.LauncherImageStorage'

EVENT_IMAGE_LOCATION = MEDIA_LOCATION + '/event_images'  # type: str
EVENT_IMAGE_STORAGE = 'custom_storages.EventImageStorage'

DEFAULT_FILE_STORAGE = DEFAULT_STORAGE

AWS_IS_GZIPPED = True

CACHALOT_TIMEOUT = 120
