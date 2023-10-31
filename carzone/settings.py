"""
Django settings for carzone project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e&wxif&s666*wxad=##+d+i9&4&oe^d(qi#sbe09$8aef_b48!' # config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # config('DEBUG', cast=bool) # True

# ALLOWED_HOSTS = [] #
ALLOWED_HOSTS = ['protected-hollows-94158-2550c71ae30d.herokuapp.com',
                 'luis-santamaria-carzone-91fe77a28602.herokuapp.com',
                 'luis-santamaria-carzone.com',
                 'www.luis-santamaria-carzone.com',
                 '127.0.0.1',]
"""
'http://127.0.0.1:8000/',
                 '127.0.0.1',
                 'localhost'
"""

# ALLOWED_HOSTS = ['*'] # Alternativa: permitir todos los hosts


SOCIALACCOUNT_LOGIN_ON_GET = True

LOGIN_REDIRECT_URL = 'accounts:dashboard'

SITE_ID = 3 # Default site id you are using in an environment ambient

# Application definition

PROJECT_APPS = [
    'pages',
    'cars',
    'accounts',
    'contacts',
]

INSTALLED_LIBRARIES = [
    'ckeditor',
    'django.contrib.humanize',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

INSTALLED_APPS.extend(PROJECT_APPS)
INSTALLED_APPS.extend(INSTALLED_LIBRARIES)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'carzone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'carzone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('POSTGRESQL_DB'),
#         'USER': config('POSTGRESQL_USER'),
#         'PASSWORD': config('POSTGRESQL_PASSWORD'),
#         'HOST': config('POSTGRESQL_HOST', default='localhost'),
#     }
# }

# DATABASES = {'default': dj_database_url.config(default=f'{config("POSTGRESQL_USER")}://{config("POSTGRESQL_USER")}:{config("POSTGRESQL_PASSWORD")}@localhost/{config("POSTGRESQL_DB")}')}
DATABASES = {'default': dj_database_url.config(default=os.environ.get("CARZONE_DB_URL"))}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'carzone/static'),
]

# Media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Autofield for Models
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Configuración de envío de correos electrónicos
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'estebanmillo700@gmail.com'
EMAIL_HOST_PASSWORD = 'cmvnbesueixltwch' # config('EMAIL_PASSWORD') #gdlmrzzpbrqaislk # 
EMAIL_USE_TLS = True

# Configuración de Whitenoise para archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# django_heroku.settings(locals())