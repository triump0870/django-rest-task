import dj_database_url

DATABASES =     {'default': dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTtTP_X_FORWARDED_PROTO','https')
try: 
        from local_settings import *
except Exception as e:
        pass
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}
python DEBUG = False
