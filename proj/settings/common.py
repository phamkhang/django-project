"""
Django settings for proj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Package to read database config from DATABASE_URL envvar.
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages'                 # file storage backend adapter
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',   # stag/prod redirect http to https
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proj.urls'

WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # MySQL
    'default': dj_database_url.config(default=
        "mysql://dghubble:password@localhost:3306/proj_dev")
    # # PostgreSQL
    # 'default': dj_database_url.config(default=
    #     "postgres://dghubble:password@localhost:5432/proj_dev")
    # # SQLite
    # 'default': dj_database_url.config(default=
    #     "sqlite:////%s" % os.path.join(BASE_DIR, 'db.sqlite3'))
}
# Point to SSL Amazon RDS public key for stag/prod environments. 
DATABASES['default']['OPTIONS'] = {'ssl': {'ca': 'proj/config/ca/rds-ssl-ca-cert.pem'}}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'STATIC_ROOT'

# Include static assets that are not tied to an app
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


