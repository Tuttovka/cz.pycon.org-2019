"""
Django settings for pyconcz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TMP_DIR = os.path.join(BASE_DIR, '..', 'tmp')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'provide in local.py'

ADMINS = [
    ('admins', 'admin@pycon.cz'),
]

# Emails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""


DEFAULT_FROM_EMAIL = 'admin@pycon.cz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [
        'cz.pycon.org',
        'pycon.cz',
    ]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',
    'import_export',

    'pyconcz.announcements',
    'pyconcz.common',
    'pyconcz.team',
    'pyconcz.proposals',
    'pyconcz.sponsors',
    'pyconcz.programme',
    'pyconcz.intermission',

    'widget_tweaks',
    'emojificate',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyconcz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'pyconcz.common.phases.phases_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyconcz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

try:
    DB_USER = os.environ['DB_USER']
    DB_HOST = os.environ['DB_HOST']
    DB_PASS = os.environ['DB_PASS']
except KeyError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'pyconcz',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': DB_HOST,
            'NAME': os.environ.get('DB_NAME', DB_USER),
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'PORT': os.environ.get('DB_PORT', 5432),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

USE_TZ = True
TIME_ZONE = 'Europe/Prague'

FORMAT_MODULE_PATH = [
    'pyconcz.formats'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/2019/static/'
STATIC_ROOT = os.path.join(TMP_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(TMP_DIR, 'media')

SLACK_WEBHOOK = ''  # This variable is set in local.py

TALKS_DATES = [datetime.date(2019, 6, 14), datetime.date(2019, 6, 15)]
WORKSHOPS_DATES = [datetime.date(2019, 6, 16)]
TALKS_ROOMS = [
    (1, 'Ballroom'),
    (2, 'Club'),
]
WORKSHOPS_ROOMS = [
    (4, 'room EB126'),
    (5, 'room EB129'),
    (6, 'room EB130'),
    (7, 'room EB226'),
    (8, 'room EB229'),
    (9, 'room EB230'),
]
SPRINT_ROOMS = [

]

OTHER_ROOMS = [
    (30, 'Foyer'),
    (40, 'Compress hall'),
    (50, 'Gallery'),
]

ALL_ROOMS = TALKS_ROOMS + WORKSHOPS_ROOMS + SPRINT_ROOMS + OTHER_ROOMS
