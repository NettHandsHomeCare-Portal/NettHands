"""
Django settings for nhhc project.

Generated by 'django-admin startproject' using Django 3.2.20.

"""

import mimetypes
import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv
from logtail import LogtailHandler
from django_redis import client

load_dotenv()
# SECTION - Basic Application Defintion
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = get_random_secret_key()
DEBUG = True
SESSION_COOKIE_SECURE = True
ADMINRESTRICT_ALLOW_PRIVATE_IP = False
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "216.24.57.1",
    "nett-hands.onrender.com",
    "www.netthandshome.care",
    "netthandshome.care",
    "0.0.0.0",
]
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
RESTRICT_ADMIN_BY_IPS = True
ALLOWED_ADMIN_IPS = os.getenv("ALLOWED_IPS")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SITE_ID = 1
ENVIRONMENT_FLOAT = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_SERVER")
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv("EMAIL_TSL_PORT")
EMAIL_HOST_USER = os.getenv("NOTIFICATION_SENDER_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_ACCT_PASSWORD")
APPEND_SLASH = True
CRISPY_TEMPLATE_PACK = "bootstrap4"
INSTALLED_APPS = [
    "kolo",
    "whitenoise.runserver_nostatic",
    # 'django_admin_env_notice',``
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    ## Installed 3rd Apps
    "coverage",
    "crispy_forms",
    "crispy_bootstrap4",
    "phonenumber_field",
    "django_prometheus",
    "request",
    "debug_toolbar",
    "localflavor",
    "captcha",
    "corsheaders",
    # "IpWhitelister",
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    ## Installed Internal Apps
    "web",
    "portal",
    "employee",
    "announcements",
    "compliance",
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "kolo.middleware.KoloMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "request.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    # "django_admin_env_notice.context_processors.from_settings",
    # "ip_restriction.IpWhitelister",
]
AUTH_USER_MODEL = "employee.Employee"
ROOT_URLCONF = "nhhc.urls"
INTERNAL_IPS = ["127.0.0.1"]
WSGI_APPLICATION = "nhhc.wsgi.application"

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/html", ".html", True)
mimetypes.add_type("text/javascript", ".js", True)

# SECTION - Database and Caching
if DEBUG:
    ENVIRONMENT_NAME = "DEVELOPMENT SERVER"
    ENVIRONMENT_COLOR = "#00FFFF"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME_DEV"),
            "USER": os.getenv("DB_USER_DEV"),
            "PASSWORD": os.getenv("DB_PASSWORD_DEV"),
            "HOST": os.getenv("DB_HOST"),
            "OPTIONS": {"sslmode": "require"},
        },
    }
else:
    REQUEST_BASE_URL = "https://www.netthandshome.care"
    ENVIRONMENT_NAME = "PRODUCTION SERVER"
    ENVIRONMENT_COLOR = "#FF2222"
    DATABASES = {
        "default": {
            "ENGINE": "django_prometheus.cache.backends.postgresql",
            "NAME": os.getenv("DB_NAME_PROD"),
            "USER": os.getenv("DB_USER_PROD"),
            "PASSWORD": os.getenv("DB_PASSWORD_PROD"),
            "HOST": os.getenv("DB_HOST"),
            "OPTIONS": {"sslmode": "require"},
        },
    }

CACHE_TTL = 60 * 15
CACHES = {
    "default": {
        "BACKEND": "django_prometheus.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_URL"),
        "OPTIONS": {
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_PREFIX": "NHHC-NATIVE",
    }
}
# CACHEOPS_REDIS=os.getenv("REDIS_URL")
# CACHEOPS_CLIENT_CLASS="django_redis.client.DefaultClient"
# CACHEOPS_DEFAULTS = {
#     'timeout': 60*15
# }
# CACHEOPS = {
#     'auth.user': {'ops': 'get', 'timeout': 60*15},
#     'auth.*': {'ops': ('fetch', 'get')},
#     'auth.permission': {'ops': 'all'},
#     '*.*': {},
# }
# !SECTION

# SECTION - Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
ADMINRESTRICT_ENABLE_CACHE = True
ADMINRESTRICT_DENIED_MSG = "Unable To Access Admin From This IP Address"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# !SECTION

# SECTION - Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_L10N = True
USE_TZ = False

DATETIME_FORMAT = "m/d/yyyy h:mm A"
ADMINS = [("Terry Brooks", "Terry@BrooksJr.com"), ("Admin", "admin@netthandshome.care")]

# SECTION -  Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "static", "vendor"),
]
# SECTION - Templates
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# !SECTION

# !SECTION

# SECTION -Logging
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} | {levelname} | {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

PRIMARY_LOG_FILE = os.path.join(BASE_DIR, "logs", "primary_ops.log")
CRITICAL_LOG_FILE = os.path.join(BASE_DIR, "logs", "fatal.log")
DEBUG_LOG_FILE = os.path.join(BASE_DIR, "logs", "utility.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))
REQUEST_LOG_USER = True
REQUEST_TRAFFIC_MODULES = [
    "request.traffic.UniqueVisitor",
    "request.traffic.UniqueVisit",
    "request.traffic.Hit",
    "request.traffic.Search",
    "request.traffic.User" "request.traffic.Error404",
    "request.traffic.Error",
]
# SECTION - Preformence Monitoring
PROMETHEUS_LATENCY_BUCKETS = (
    0.1,
    0.2,
    0.5,
    0.6,
    0.8,
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.5,
    9.0,
    12.0,
    15.0,
    20.0,
    30.0,
    float("inf"),
)
PROMETHEUS_METRIC_NAMESPACE = "nhhc"
