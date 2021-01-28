from ndemo.settings.common import *

SECRET_KEY = 'l6ypqe5be68n@b40+(9yo0!0e9j*o-8(+2)^^mg173*cy=tybn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES ['default'] = dj_database_url.config ()

DATABASES = {
 "default": 
 {
  "ENGINE": "django.db.backends.postgresql_psycopg2", #one of those should work
  'ENGINE': 'django.db.backends.postgresql',   #one of those should work
  "NAME": 'd9q4fnpf64jds1',
  "HOST": "ec2-52-2-6-71.compute-1.amazonaws.com", 
  "PORT": "5432",
  "PASSWORD":"3d7ef536f0c19e750fb4cf001bf5f8d3f3cfef7394302953ffb18db0a206d2b9",
  "user":"vlkbgtdxdzqwhu"
  
 }
 }
