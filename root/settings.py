import os
from os import getenv
from os.path import join
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-f1%g5q-6^9pgbz6sf!beupt2=3-)#+t3s)g!)j*j+e3o569*e6'

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
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

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'root.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv("DB_NAME"),
        'USER': getenv("DB_USER"),
        'PORT': getenv("DB_PORT"),
        'HOST': getenv("DB_HOST"),
        'PASSWORD': getenv("DB_PASSWORD"),
    }
}


# Password validation

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


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ========== MinIO / S3 Saqlash Konfiguratsiyasi ==========

# MinIO Server Ma'lumotlari
MINIO_ENDPOINT = 'localhost:9000'  # Ishlab chiqarish uchun o'zgartiring
MINIO_ACCESS_KEY = 'minioadmin'
MINIO_SECRET_KEY = 'minioadmin'
MINIO_BUCKET_NAME = 'django-media'
MINIO_USE_HTTPS = False  # Ishlab chiqarishda HTTPS bilan True qo'ying

# AWS S3 Konfiguratsiyasi (django-storages uchun)
AWS_ACCESS_KEY_ID = MINIO_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = MINIO_SECRET_KEY
AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
AWS_S3_ENDPOINT_URL = f'http{"s" if MINIO_USE_HTTPS else ""}://{MINIO_ENDPOINT}'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_CUSTOM_DOMAIN = f'{MINIO_BUCKET_NAME}.{MINIO_ENDPOINT}' if not MINIO_USE_HTTPS else None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'media'
AWS_DEFAULT_ACL = 'public-read'

# Statik Fayllar Konfiguratsiyasi
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media Fayllar Konfiguratsiyasi
MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# MinIO dan fayl saqlashdan foydalaning

STORAGES = {
    "default": {
        "BACKEND": "root.storages.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Public emas, private saqlash
# AWS_DEFAULT_ACL = 'private'
AWS_QUERYSTRING_AUTH = True  # URL larga imzo (signature) qo'shadi
AWS_QUERYSTRING_EXPIRE = 5  # havola 1 soatdan keyin eskiradi (sekundlarda)