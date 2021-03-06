"""
Django settings for SampleDB2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# we are filtering warnings that tend to come up in running populate.py
import warnings
import exceptions
warnings.filterwarnings("ignore", category=exceptions.RuntimeWarning, module='django.db.models.fields', lineno=900)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3#d-g6g@kva0au8smne=_pjyc_++9@nw2kr+k#j37y!3j8_2mv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# needed to relax this so the site gets served without permission
# errors, see also https://stackoverflow.com/questions/20321673/debugging-apache-django-wsgi-bad-request-400-error
ALLOWED_HOSTS = ['phy-lmsrv2', 'localhost', 'phy-lmsrv2.ex.ac.uk',
                 '.ex.ac.uk']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
	'samples',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SampleDB2.urls'

WSGI_APPLICATION = 'SampleDB2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASE_HOST = ''
#look for database host in environment variable
DATABASE_HOST = os.getenv('PYME_DATABASE_HOST','DBSRV1')
DATABASE_USER = os.getenv('PYME_DATABASE_USER','sample_db')
DATABASE_PWD = os.getenv('PYME_DATABASE_PWD','PYMEUSER')

DATABASES = {
	'default': {
        'NAME': 'sample_db',
        'HOST' : DATABASE_HOST,
        'ENGINE': 'django.db.backends.mysql',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PWD,
        'OPTIONS': {"connect_timeout": 5,},
    },
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'
STATIC_URL = '/media/'
STATIC_ROOT = '/var/www/SampleDB/static/'

AUTOCOMPLETE_MEDIA_PREFIX = '/media/autocomplete/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'media'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
