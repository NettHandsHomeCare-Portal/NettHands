"""
Django settings for nhhc project.

Generated by 'django-admin startproject' using Django 3.2.20.

"""

import json
import mimetypes
import os
from pathlib import Path

import highlight_io
from django.core.management.utils import get_random_secret_key
from django_redis import client
from dotenv import load_dotenv
from highlight_io.integrations.django import DjangoIntegration
from logtail import LogtailHandler
from loguru import logger

from nhhc.private_key import PRIVATE_KEY

# SECTION - Basic Application Defintion
OFFLINE = False
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True
DATETIME_FORMAT = "m/d/yyyy h:mm A"
ADMINS = [("Terry Brooks", "Terry@BrooksJr.com")]
CSRF_COOKIE_NAME = "nhhc-csrf"
CSRF_USE_SESSIONS = True
SESSION_COOKIE_NAME = "nhhc-session"
SESSION_COOKIE_SECURE = True
ROBOTS_USE_HOST = False

ADMINRESTRICT_ALLOW_PRIVATE_IP = False
FIRST_DAY_OF_WEEK = 1
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "216.24.57.1",
    "nett-hands.onrender.com",
    "www.netthandshome.care",
    "netthandshome.care",
    "0.0.0.0",
]
ROBOTS_SITEMAP_VIEW_NAME = "cached-sitemap"
CSRF_FAILURE_VIEW = "web.views.csrf_failure"
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
RESTRICT_ADMIN_BY_IPS = True
ALLOWED_ADMIN_IPS = os.getenv("ALLOWED_IPS")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SITE_ID = 1
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24

ENVIRONMENT_FLOAT = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_SERVER")
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv("EMAIL_TSL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_ACCT_PASSWORD")
APPEND_SLASH = True
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    "bootstrap",
    "uni_form",
    "bootstrap5",
    "bootstrap4",
)

CRISPY_TEMPLATE_PACK = "bootstrap5"
INSTALLED_APPS = [
    "kolo",
    "whitenoise.runserver_nostatic",
    "allauth",
    "allauth.account",
    "django_admin_env_notice",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    ## Installed 3rd Apps
    "coverage",
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "phonenumber_field",
    "widget_tweaks",
    "django_prometheus",
    "rest_framework",
    "rest_framework.authtoken",
    "request",
    "formset",
    "django_filters",
    "debug_toolbar",
    "localflavor",
    "captcha",
    "corsheaders",
    "easy_thumbnails",
    "filer",
    "robots",
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
    "authentication",
    "compliance",
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "kolo.middleware.KoloMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # "nhhc.middleware.PasswordChangeMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "request.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
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
CACHE_TTL = 60 * 15

if DEBUG:
    SITE_ID = 1
    ENVIRONMENT_NAME = "DEVELOPMENT SERVER"
    ENVIRONMENT_COLOR = "#00FFFF"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DEV_DATABASE"),
            "USER": os.getenv("POSTGRES_DEV_USER"),
            "PASSWORD": os.getenv("POSTGRES_DEV_PASSWORD"),
            "PORT": 5432,
            "HOST": os.getenv("POSTGRES_HOST"),
            "OPTIONS": {"sslmode": "require"},
        },
    }

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }
else:
    SITE_ID = 3
    REQUEST_BASE_URL = "https://www.netthandshome.care"
    ENVIRONMENT_NAME = "PRODUCTION SERVER"
    ENVIRONMENT_COLOR = "#FF2222"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_PROD_DATABASE"),
            "USER": os.getenv("POSTGRES_PROD_USER"),
            "PASSWORD": os.getenv("POSTGRES_PROD_PASSWORD"),
            "PORT": "5432",
            "HOST": os.getenv("POSTGRES_HOST"),
            "OPTIONS": {"sslmode": "require"},
        },
    }
    CACHES = {
        "default": {
            "BACKEND": "django_prometheus.cache.backends.redis.RedisCache",
            "LOCATION": os.getenv("REDIS_CACHE_URI"),
            "OPTIONS": {
                "PARSER_CLASS": "redis.connection.HiredisParser",
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            "KEY_PREFIX": "NHHC-NATIVE",
        }
    }

# !SECTION

# SECTION - Password validation
AUTH_PROFILE_MODULE = "authentication.UserProfile"
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
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = "/dashboard"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Nett Hands Employee Portal"


# SECTION - Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_L10N = True
USE_TZ = False


# !SECTION

# SECTION - STORAGE

STORAGE_DESTINATION = os.getenv("STORAGE_DESTINATION")
FILE_UPLOAD_TEMP_DIR = BASE_DIR / "tmp"
if STORAGE_DESTINATION == "s3":
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "private"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    AWS_QUERYSTRING_EXPIRE = 3600
    AWS_S3_REGION_NAME = "us-east-2"
    AWS_CLOUDFRONT_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_CLOUDFRONT_KEY = PRIVATE_KEY
    # s3 static settings
    STATIC_LOCATION = "staticfiles"
    STATIC_URL = f"https://cdn.netthandshome.care/{STATIC_LOCATION}/"
    STATIC_ROOT = STATIC_URL
    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
    )
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "nhhc.storage_backends.PublicMediaStorage"
    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = "restricted"
    MEDIA_DIRECTORY = "/restricted/compliance"
    PRIVATE_FILE_STORAGE = "nhhc.storage_backends.PrivateMediaStorage"

    FILER_STORAGES = {
        "private": {
            "hhg-oig": {
                "ENGINE": "fnhhc.storage_backends.PrivateMediaStorage",
                "OPTIONS": {
                    "location": f"https://{AWS_S3_CUSTOM_DOMAIN}/{PRIVATE_MEDIA_LOCATION}",
                    "base_url": "/smedia/filer/",
                },
                "UPLOAD_TO": "filer.utils.generate_filename.randomized",
                "UPLOAD_TO_PREFIX": "filer_public",
            },
        }
    }
else:
    STATIC_URL = "/staticfiles/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    MEDIA_URL = "/mediafiles/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# SECTION - File Management
FILER_ADD_FILE_VALIDATORS = {
    "text/html": ["filer.validation.deny_html"],
    "image/svg+xml": ["filer.validation.deny"],
}
FILER_UPLOADER_MAX_FILE_SIZE = 2
FILER_MIME_TYPE_WHITELIST = [
    "text/plain",
    "application/pdf",
    "image/*",
]

FILER_ADD_FILE_VALIDATORS["aspx"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["asp"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["css"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["swf"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["xhtml"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["rhtml"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["jsp"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["js"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["pl"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["php"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["cgi"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["py"] = ["filer.validation.deny"]
FILER_ADD_FILE_VALIDATORS["xml"] = ["filer.validation.deny"]

#! SECTION

# SECTION -  Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "static", "vendor"),
]
# SECTION - Templates
TEMPLATE_DIR = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "web", "templates"),
    os.path.join(BASE_DIR, "employee", "templates"),
    os.path.join(BASE_DIR, "authentication", "templates"),
    os.path.join(BASE_DIR, "portal", "templates"),
    os.path.join(BASE_DIR, "compliance", "templates"),
    os.path.join(BASE_DIR, "announcements", "templates"),
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIR,
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
HIGHLIGHT_MOINITORING = highlight_io.H(
    "jdkmrpog",
    integrations=[DjangoIntegration()],
    instrument_logging=True,
    service_name="netthands-app",
    service_version="git-sha",
    environment="development",
)
PRIMARY_LOG_FILE = os.path.join(BASE_DIR, "logs", "primary_ops.log")
CRITICAL_LOG_FILE = os.path.join(BASE_DIR, "logs", "fatal.log")
DEBUG_LOG_FILE = os.path.join(BASE_DIR, "logs", "utility.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))

logger.add(
    HIGHLIGHT_MOINITORING.logging_handler,
    format="{message}",
    level="DEBUG",
    backtrace=True,
    serialize=True,
)


logger.add(DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG")
logger.add(PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO")
logger.add(LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO")

REQUEST_LOG_USER = True
REQUEST_TRAFFIC_MODULES = [
    "request.traffic.UniqueVisitor",
    "request.traffic.UniqueVisit",
    "request.traffic.Hit",
    "request.traffic.Search",
    "request.traffic.User" "request.traffic.Error404",
    "request.traffic.Error",
]
# SECTION - Preformence MonitoringSCOUT_MONITOR
SCOUT_MONITOR = True
SCOUT_NAME = "nhhc"
SCOUT_KEY = os.getenv("SCOUT_KEY")
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

# SECTION  - REST API CONFIGURATIONS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Nett Hands Control Center",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Control Center",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Control Center",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo-light.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo-dark.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "img/favicon.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Control Center",
    # Copyright on the footer
    "copyright": "Blackberry Py, LLC",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["authentication.Employee", "auth.Group"],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "authentication.Employee"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "authentication.Employee"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["sites", "robots"],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # Custom links to append to app groups, keyed on app name
    "order_with_respect_to": [""],
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gall2ery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "authentication.Employee": "fas fa-user",
        "auth.Group": "fas fa-users",
        "authentication.tokens": "fa-solid fa-certificate",
        "authentication.UserProfiles": "fa-solid fa-id-badge",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}
