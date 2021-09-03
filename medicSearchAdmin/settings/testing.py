import os

from .settings import *

DEBUG = True

#cria uma secret key para o ambiente de teste
SECRET_KEY = 'm2f^^mc(3izq@9(mc8#)hv2kxaiql6c_)$2t6o33jzx=uerh1d'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}