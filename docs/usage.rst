=====
Usage
=====

To use Django Dropbox Upload Handler in a project, add it to your `INSTALLED_APPS`:

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
