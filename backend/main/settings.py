from pathlib import Path
import decouple

import os

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = decouple.config('DJANGO_DEBUG')

# set SECRET_KEY based on value of DEBUG
if DEBUG:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = decouple.config('DJANGO_SECRET_KEY_DEVELOPMENT')
else:
    SECRET_KEY = decouple.config('DJANGO_SECRET_KEY_PRODUCTION')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'appliances',
    'accessories',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Use custom user model for authentication
AUTH_USER_MODEL = 'users.User'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.SafeJWTAuthentication',
    ]
}


# Secret for encoding User refresh tokens
REFRESH_TOKEN_SECRET = decouple.config('DJANGO_REFRESH_TOKEN_SECRET')

# define refresh token lifetime
REFRESH_TOKEN_EXPIRY = {
    'days': 7,
    'hours': 0,
    'minutes': 0,
    'seconds': 0
}

# define refresh token lifetime
ACCESS_TOKEN_EXPIRY = {
    'days': 0,
    'hours': 0,
    'minutes': 0,
    'seconds': 10
}
# to accept cookies via axios
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    # other whitelisted origins
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    # other allowed origins...
]

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    # other allowed hosts...
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    # other allowed origins...
]

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'refresh_token',
    'x-csrftoken',
    'x-xsrftoken',
    'withcredentials'
]

