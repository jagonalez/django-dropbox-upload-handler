# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django_dropbox_upload_handler.urls import urlpatterns as django_dropbox_upload_handler_urls

urlpatterns = [
    url(r'^', include(django_dropbox_upload_handler_urls, namespace='django_dropbox_upload_handler')),
]
