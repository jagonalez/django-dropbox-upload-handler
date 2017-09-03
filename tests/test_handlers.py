#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-dropbox-upload-handler
------------

Tests for `django-dropbox-upload-handler` models module.
"""

from django.test import TestCase, RequestFactory, Client
from django.conf import settings
from django_dropbox_upload_handler.handler import DropboxFileUploadHandler, DropboxFile
from django.core.cache import cache
import dropbox
import os
import json

class TestDjango_dropbox_upload_handler(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.dropbox = dropbox.Dropbox(settings.DROPBOX_UPLOAD_HANDLER['ACCESS_TOKEN'])
        self.file_path = settings.DROPBOX_UPLOAD_HANDLER['UPLOAD_PATH'] + 'test.txt'
        self.file = 'tests/test.txt'

    def test_upload(self):
        with open(self.file) as fp:
            request = self.factory.post('/upload', {'name': 'test.txt', 'file': fp})
            request.upload_handlers.insert(0, DropboxFileUploadHandler(request))
            files = request.FILES
            self.assertIsInstance(files['file'], DropboxFile)
            metadata = self.dropbox.files_get_metadata(self.file_path)
            self.assertEqual(metadata.name, 'test.txt')

    def test_progress_upload(self):
        with open(self.file, 'rb') as fp:
            progress_id = 'XXXXX'
            contents = fp.read()

            request = self.factory.post('/upload?progress_id=' + progress_id)
            cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
            content_length = len(contents)

            handler = DropboxFileUploadHandler(request)

            handler.new_file("file", 'test.txt', "text/plain", content_length, None, None)
            result = handler.handle_raw_input(None, None, content_length, None, None)

            data = cache.get(cache_key)

            self.assertIsNotNone(data)
            self.assertEqual(data['uploaded'], 0)
            self.assertEqual(data['length'], content_length)

            done = handler.receive_data_chunk(contents, 0)
            f = handler.file_complete(content_length)
            updated_data = cache.get(cache_key)
            self.assertIsNotNone(updated_data)
            self.assertEqual(updated_data['uploaded'], content_length)

            c = Client()
            response = c.get('/upload_progress?progress_id=' + progress_id)
            content = json.loads(response.content)

            self.assertIsNotNone(content)
            self.assertIsNotNone(content["uploaded"], content_length)

            handler.upload_complete()
            data = cache.get(cache_key)
            self.assertIsNone(data)

            response = c.get('/upload_progress?progress_id=' + progress_id)
            self.assertEqual(response.status_code, 201)


    def tearDown(self):
        try:
            self.dropbox.files_delete(self.file_path)
        except:
            pass
