# -*- coding: utf-8 -*-
# настройки для проекта helloworld

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_helloworld',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []
TIME_ZONE = 'Europe/Moscow'  # наше время
LANGUAGE_CODE = 'ru-RU'  # по-русски
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# статика
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'c43pfz($k1l47_9dyu1++js##7(tbjw+83!=23@d%2cjd6%=8-'

# шаблоны
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'helloworld.urls'
WSGI_APPLICATION = 'helloworld.wsgi.application'

# папки с шаблонами
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    os.path.join(PROJECT_ROOT, '../flatpages/templates'),
)

# установленные приложения
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'flatpages', 
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# логи (хз зачем, но пусть будет)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
    }
}