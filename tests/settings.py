# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

DROPBOX_UPLOAD_HANDLER = {
    'ACCESS_TOKEN': '',
    'UPLOAD_PATH': '/test/'
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
FILE_UPLOAD_HANDLERS = [
    'django_dropbox_upload_handler.handler.DropboxFileUploadHandler'
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_dropbox_upload_handler",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
