import os
import sys
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV_FILE = BASE_DIR.joinpath('.env')
if DOTENV_FILE.is_file():
    dotenv.load_dotenv(str(DOTENV_FILE))

SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False
if DEBUG is True:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['weitingyang.pythonanywhere.com']
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'widget_tweaks',
    'rest_framework',
    'corsheaders',
    'coverage',

    'home.apps.HomeConfig',
    'shop.apps.ShopConfig',
    'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Application configuration
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'https://weitingyang.pythonanywhere.com',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}


# Database
"""
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRESQL_NAME'],
            'USER': os.environ['POSTGRESQL_USER'],
            'PASSWORD': os.environ['POSTGRESQL_PASSWORD'],
            'HOST': os.environ['POSTGRESQL_HOST'],
            'PORT': '5432',
        },
        'test': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Auth
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

LOGIN_REDIRECT_URL = '/'


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATIC_URL = '/static/'

STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
