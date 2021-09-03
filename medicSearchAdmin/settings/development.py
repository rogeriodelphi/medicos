import os

from .settings import *

DEBUG = True

#cria uma secret key para o ambiente de desenvolvimento
SECRET_KEY = 'wp#-n%plnwu$1zwt0+-v8vcr_u!xmo=*v+-%cumkw-e5@-!0tj'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}