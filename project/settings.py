import os

import dj_database_url
import environ
import redis

root = environ.Path(__file__, "../..")

os.sys.path.insert(0, root())
os.sys.path.insert(0, os.path.join(root(), "apps"))

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "oiph!k9a+8p_&vpev0*sch^en7#ip&5v6gybt%=(8b+$-qbzs&"),
    ALLOWED_HOSTS=(list, ["*"]),
    DB_DSN=(str, "sqlite:///db.sqlite3"),
    REDIS_DSN=(str, "redis://localhost:6379"),
    BASE_URL=(str, "http://localhost:8000"),
    CUTTLY_API_KEY=(str, None),
    ROLE=(str, "prod"),
    RECAPTCHA_PUBLIC_KEY=(str, None),
    RECAPTCHA_PRIVATE_KEY=(str, None),
)

ini_file_path = root(".env")
if os.path.exists(ini_file_path):
    env.read_env(ini_file_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROLE = env("ROLE")

CUTTLY_API_KEY = env("CUTTLY_API_KEY")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    "django_dramatiq",
    "corsheaders",
    "admin_honeypot",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    "django_filters",
    "rest_framework",
    "djoser",
    "rest_framework.authtoken",
    'apps.api.apps.ApiConfig',
    'apps.common.apps.CommonConfig',
    'apps.link.apps.LinkConfig',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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
APPEND_SLASH = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "WARNING", "handlers": ["console"]},
    "formatters": {"verbose": {"format": "%(levelname)s  %(asctime)s  %(module)s: %(message)s"}},
    "handlers": {"console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"}},
    "loggers": {
        "django.server": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "django.request": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "django.db.backends": {"level": "ERROR", "handlers": ["console"], "propagate": False},
    },
}

REST_FRAMEWORK_EXTENSIONS = {"DEFAULT_CACHE_RESPONSE_TIMEOUT": 1}
REST_FRAMEWORK = {
    "PAGE_SIZE": 20,
    "UPLOADED_FILES_USE_URL": env("ROLE") != "test",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "apps.api.authentications.CsrfExemptSessionAuthentication",
    ],
}

DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {"connection_pool": redis.ConnectionPool.from_url(env("REDIS_DSN"))},
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.AdminMiddleware",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
    ]
}

if ROLE == "test":

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
