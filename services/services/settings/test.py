from .base import *  # noqa


DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'seriviceone',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'coderslab',
    }
}