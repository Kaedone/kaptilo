import os

import dj_database_url
import environ

root = environ.Path(__file__, "../..")

os.sys.path.insert(0, root())
os.sys.path.insert(0, os.path.join(root(), "apps"))

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "oiph!k9a+8p_&vpev0*sch^en7#ip&5v6gybt%=(8b+$-qbzs&"),
    ALLOWED_HOSTS=(list, ["*"]),
    DB_DSN=(str, "sqlite:///db.sqlite3"),
    BASE_URL=(str, "http://localhost:8000"),
    API_KEY=(str, None),
    ROLE=(str, "prod"),
    RECAPTCHA_PUBLIC_KEY=(str, None),
    RECAPTCHA_PRIVATE_KEY=(str, None),
)

ini_file_path = root(".env")
if os.path.exists(ini_file_path):
    env.read_env(ini_file_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROLE = env("ROLE")

API_KEY = env("API_KEY")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

INSTALLED_APPS = [
    'captcha_admin',
    'captcha',
    "admin_honeypot",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'apps.common.apps.CommonConfig',
    'apps.link.apps.LinkConfig',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {"default": dj_database_url.config(default=env("DB_DSN"))}

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

USE_TZ = True
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

MEDIA_URL = "/media/"
MEDIA_ROOT = root("media")

STATIC_URL = "/static/"
STATIC_ROOT = root("static")
STATICFILES_DIRS = [root("project/static")]

BASE_URL = env("BASE_URL")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")

if ROLE == "test":

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
