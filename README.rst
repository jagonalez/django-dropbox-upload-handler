=============================
Django Dropbox Upload Handler
=============================

.. image:: https://badge.fury.io/py/django-dropbox-upload-handler.svg
    :target: https://badge.fury.io/py/django-dropbox-upload-handler

.. image:: https://travis-ci.org/jagonalez/django-dropbox-upload-handler.svg?branch=master
    :target: https://travis-ci.org/jagonalez/django-dropbox-upload-handler

.. image:: https://codecov.io/gh/jagonalez/django-dropbox-upload-handler/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jagonalez/django-dropbox-upload-handler

Transfer Uploaded Files to Dropbox

Documentation
-------------

The full documentation is at https://django-dropbox-upload-handler.readthedocs.io.

Quickstart
----------

Install Django Dropbox Upload Handler::

    pip install django-dropbox-upload-handler

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_dropbox_upload_handler.apps.DjangoDropboxUploadHandlerConfig',
        ...
    )

Add Django Dropbox Upload Handler's URL patterns:

.. code-block:: python

    from django_dropbox_upload_handler import urls as django_dropbox_upload_handler_urls


    urlpatterns = [
        ...
        url(r'^', include(django_dropbox_upload_handler_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
