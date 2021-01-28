from ndemo.settings.common import *

SECRET_KEY = 'l6ypqe5be68n@b40+(9yo0!0e9j*o-8(+2)^^mg173*cy=tybn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



DATABASES = {
    '"default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
