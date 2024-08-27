
from pathlib import Path
from django.conf import settings
import os
from decouple import config 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-2mh6-i_o(tqo(++kos_uto4r1e+c+iv)79ch3o(6=47+p&i!@v'
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = []  # Replace with your domain in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'storages',  # Required for using S3 as storage
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add directories for template files if needed
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

WSGI_APPLICATION = 'myproject.wsgi.application'
LOGIN_REDIRECT_URL = '/login/'

# Database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',  # This will create a db.sqlite3 file in your BASE_DIR
#     }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Database name
        'USER': 'postgres.aklufpgvdkyktpwrhxzk',
        'PASSWORD': 'Mi4mgVLr1bLseftb',  # Replace with your actual password
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '6543',  # Port for connection pooling (pgbouncer)
        'OPTIONS': {
            'sslmode': 'require',  # Ensure SSL is used for the connection
        },
    }
}



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# AWS S3 settings for both development and production
# Static files (CSS, JavaScript, Images)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AUTH_USER_MODEL = 'myapp.CustomUser'
AWS_ACCESS_KEY_ID = 'AKIAZI2LFMFHJFBNQYWG'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'akskdsjkhfk'
AWS_S3_REGION_NAME = 'us-east-1'# Change region as needed
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
# Media settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'