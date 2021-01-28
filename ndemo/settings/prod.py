from ndemo.settings.common import *

SECRET_KEY = 'l6ypqe5be68n@b40+(9yo0!0e9j*o-8(+2)^^mg173*cy=tybn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ndemo_db',
        }
    }
DATABASES ['default'] = dj_database_url.config ()
