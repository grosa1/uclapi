"""
Django settings for uclapi project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import requests
from distutils.util import strtobool

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# This value should be set by the UCLAPI_PRODUCTION environment
# variable anyway. If in production, debug should be false.
DEBUG = not strtobool(os.environ.get("UCLAPI_PRODUCTION"))

ALLOWED_HOSTS = ["localhost"]

# If a domain is specified then make this an allowed host
if os.environ.get("UCLAPI_DOMAIN"):
    ALLOWED_HOSTS.append(os.environ.get("UCLAPI_DOMAIN"))

# If we are running under the AWS Elastic Load Balancer then enable internal
# requests so that the ELB and Health Checks work
if strtobool(os.environ.get("UCLAPI_RUNNING_ON_AWS_ELB")):
    EC2_PRIVATE_IP = None
    try:
        EC2_PRIVATE_IP = requests.get(
            "http://169.254.169.254/latest/meta-data/local-ipv4",
            timeout=0.01
        ).text
    except requests.exceptions.RequestException:
        pass

    if EC2_PRIVATE_IP:
        ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dashboard',
    'marketplace',
    'roombookings',
    'oauth',
    'timetable',
    'common',
    'raven.contrib.django.raven_compat',
    'corsheaders',
    'workspaces',
    'webpack_loader'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.append(
        'dashboard.middleware.fake_shibboleth_middleware'
        '.FakeShibbolethMiddleWare'
    )

ROOT_URLCONF = 'uclapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'uclapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_UCLAPI_NAME"),
        'USER': os.environ.get("DB_UCLAPI_USERNAME"),
        'PASSWORD': os.environ.get("DB_UCLAPI_PASSWORD"),
        'HOST': os.environ.get("DB_UCLAPI_HOST"),
        'PORT': os.environ.get("DB_UCLAPI_PORT")
    },
    'roombookings': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': os.environ.get("DB_ROOMS_NAME"),
        'USER': os.environ.get("DB_ROOMS_USERNAME"),
        'PASSWORD': os.environ.get("DB_ROOMS_PASSWORD"),
        'HOST': '',
        'PORT': ''
    },
    'gencache': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_CACHE_NAME"),
        'USER': os.environ.get("DB_CACHE_USERNAME"),
        'PASSWORD': os.environ.get("DB_CACHE_PASSWORD"),
        'HOST': os.environ.get("DB_CACHE_HOST"),
        'PORT': os.environ.get("DB_CACHE_PORT")
    }
}

DATABASE_ROUTERS = ['uclapi.dbrouters.ModelRouter']

RAVEN_CONFIG = {
    'dsn': os.environ.get("SENTRY_DSN"),
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Cross Origin settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/roombookings/.*$'

# Fair use policy
fair_use_policy_path = os.path.join(
    BASE_DIR,
    'uclapi/UCLAPIAcceptableUsePolicy.txt'
)
with open(fair_use_policy_path, 'r', encoding='utf-8') as fp:
    FAIR_USE_POLICY = list(fp)

REDIS_UCLAPI_HOST = os.environ["REDIS_UCLAPI_HOST"]

# Celery Settings
CELERY_BROKER_URL = 'redis://' + REDIS_UCLAPI_HOST
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

ROOMBOOKINGS_SETID = 'LIVE-18-19'

# We need to specify a tuple of STATICFILES_DIRS instead of a
# STATIC_ROOT so that collectstatic picks up the WebPack bundles
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# S3 file storage settings
# There are three scenarios to consider:
# 1) Local development
#    In local dev,  AWS_S3_STATICS = False
#                   AWS_S3_STATICS_CREDENTIALS_ENABLED = False
#    These allow you to use local statics using /static/ in the
#    same way as you would normally.
# 2) Production
#    In prod,       AWS_S3_STATICS = True
#                   AWS_S3_STATICS_CREDENTIALS_ENABLED = False
#    This means that S3 statics will be used, but no creds are
#    needed on the boxes because web servers should never do
#    uploads to the remote S3 bucket.
# 3) Deployment
#    In deployment, AWS_S3_STATICS = True
#                   AWS_S3_STATICS_CREDENTIALS_ENABLED = True
#    This will be done either from CI/CD or from the computer
#    of a person who has permission to upload new statics to
#    S3.

if strtobool(os.environ.get("AWS_S3_STATICS", "False")):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]
    AWS_LOCATION = os.environ["AWS_S3_BUCKET_PATH"]
    AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION"]

    # This is a hack to not require AWS Access Credentials
    # when the system is running in the Cloud. This avoids us from
    # needing to store AWS credentials.
    # https://github.com/jschneier/django-storages/issues/254#issuecomment-329813295  # noqa
    AWS_S3_CUSTOM_DOMAIN = "{}.s3.amazonaws.com".format(
        AWS_STORAGE_BUCKET_NAME
    )

    # We set the default ACL data on all stacks we upload to public-read
    # so that the files are world readable.
    # This is required for the statics to be served up directly.
    # Often this is a security risk, but in this case it's
    # actually required to serve the website.
    AWS_DEFAULT_ACL = "public-read"

    # If credentials are enabled, collectstatic can do uploads
    if strtobool(os.environ["AWS_S3_STATICS_CREDENTIALS_ENABLED"]):
        AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
        AWS_SECRET_ACCESS_KEY = os.environ["AWS_ACCESS_SECRET"]
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }
        AWS_S3_ENCRYPTION = False
    else:
        AWS_QUERYSTRING_AUTH = False

    # Since we are hosting on AWS, we should set the Static URL to it
    STATIC_URL = "{}/{}".format(
        AWS_S3_CUSTOM_DOMAIN,
        AWS_LOCATION
    )
    # Set up the WebPack loader for remote loading
    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': not DEBUG,
            'BUNDLE_DIR_NAME': './',  # must end with slash
            'STATS_URL': "{}/webpack-stats.json".format(STATIC_URL),
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
            'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
        }
    }
else:
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    # The default Static URL is /static/ which is fine for when statics
    # have been built and placed into their respective folders.
    STATIC_URL = os.environ.get("STATIC_URL", '/static/')

    # Set up the WebPack loader for local loading
    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': not DEBUG,
            'BUNDLE_DIR_NAME': './',  # must end with slash
            'STATS_FILE': os.path.join(
                BASE_DIR,
                'static',
                'webpack-stats.json'
            ),
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
            'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
        }
    }
