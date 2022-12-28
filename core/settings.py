"""
Ajustes de Django para el proyecto.

Generado al comenzar el proyecto con: 'django-admin startproject' utilizando Django 4.1.4.

https://docs.djangoproject.com/en/4.1/topics/settings/

https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# crea la ruta dentro del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# variables de ambiente (clave secreta: se genera aleatoriamente con cada proyecto)
SECRET_KEY = 'django-insecure-#ualgckcpcpq8+_w_-5px0pkmxfll)by+z%9-046e%51-8h1bf' # os.environ.get('SECRET_KEY')

# no ejecutar con Debug = True en produccion / no se debe desplegar el sitio con Debug = True
DEBUG = True # os.environ.get('DEBUG')

# lista de hosts/dominios del sitio
ALLOWED_HOSTS = ['6183-2800-300-8221-88f0-00-1c.sa.ngrok.io','127.0.0.1']

# aplicaciones instaladas en el sitio
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

# un middleware es un software con el que las distintas aplicaciones se comunican entre si
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# representa la ruta de importacion a la configuracion de URL
ROOT_URLCONF = 'core.urls'

# contiene las configuraciones para las plantillas a utilizar
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # base_dir apunta a la ruta, template especifica la carpeta 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ruta de la aplicacion WSGI 
WSGI_APPLICATION = 'core.wsgi.application'

# contiene las configuraciones para las bases de datos 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# validadores para checkear la seguridad de las passwords de usuario
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# representa el codigo del lenguaje
LANGUAGE_CODE = 'en-us'

# representa la zona horaria para la aplicacion
TIME_ZONE = 'UTC'

# debe estar en True para que haga efecto el cambio de idioma
USE_I18N = True

# zona horaria por defecto de Django
USE_TZ = True

# ruta para archivos estaticos como CSS, JavaScript e Imagenes
STATIC_URL = 'static/'

# llave primaria a usar para modelos que no tienen un campo con 'primary_key = True'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
