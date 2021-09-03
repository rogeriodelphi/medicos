import os

from .settings import *

DEBUG = True

#cria uma secret key para o ambiente de produção
SECRET_KEY = 'a+w!z!jk5hg!ygviqgoc-zs9l$o2(63#5kylc-&&wsd+@zm(+g'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}