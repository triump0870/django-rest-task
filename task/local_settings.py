from settings import *
from os.path import join
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': 'Movie@0870',
        'PORT': '5432'
    }
}

#STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
STATIC_ROOT = join(BASE_DIR, 'static')
