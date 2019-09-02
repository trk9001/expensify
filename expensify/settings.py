import os

# Django's standard settings --------------------------------------------------

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

INSTALLED_APPS = [
    # built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'crispy_forms',

    # this project's apps
    'core.apps.CoreConfig',
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

ROOT_URLCONF = 'expensify.urls'

SECRET_KEY = 'q#x^cdqs6gs0$r3fm_lctq#ifae_@h#!nq5-98dh61uozpxoy+'

SHORT_DATE_FORMAT = 'T/m/d'
SHORT_DATETIME_FORMAT = 'T/m/d P'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'expensify.wsgi.application'

# Django's auth framework's login settings
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

# Management of static and user-uploaded files
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Internationalization/localization settings
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 3rd party settings ----------------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# -----------------------------------------------------------------------------

# Allow local_settings.py to override settings, if it exists
try:
    from .local_settings import *
except ImportError:
    pass
