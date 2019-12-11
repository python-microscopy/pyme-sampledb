# pyme-sampledb
Django database web app for tracking slide and sample information. Integrates with PYMEAcquire to automatically link 
acquisitons and metadata in a searchable manner.

See http://python-microscopy.org/doc/SampleDB.html for details (TODO - move the docs into this repo)

**WARNING:** As with any Django app, change the secrets in settings.py before deploying. You might also want to change the ``DEBUG`` and ``ALLOWED_HOSTS`` settings. 
