import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, 'subdir').
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Open configuration files
with open(os.path.join(BASE_DIR, 'config', 'development.json')) as file:
    configuration = json.loads(file.read())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = configuration['DJANGO']['SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = configuration['DJANGO']['DEBUG']

ALLOWED_HOSTS = configuration['DJANGO']['ALLOWED_HOSTS']


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

PROJECT_APPS = [
    'apps.finances.apps.FinancesConfig',
    'apps.stocks.apps.StocksConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': configuration['DATABASE']['ENGINE'],
        'NAME': os.path.join(BASE_DIR, configuration['DATABASE']['NAME']),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
PASSWORD_VALIDATORS = [
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    'django.contrib.auth.password_validation.MinimumLengthValidator',
    'django.contrib.auth.password_validation.CommonPasswordValidator',
    'django.contrib.auth.password_validation.NumericPasswordValidator'
]


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': validator for validator in PASSWORD_VALIDATORS}]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = configuration['DJANGO']['LANGUAGE_CODE']

TIME_ZONE = configuration['DJANGO']['TIME_ZONE']

USE_I18N = configuration['DJANGO']['USE_I18N']

USE_TZ = configuration['DJANGO']['USE_TZ']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
