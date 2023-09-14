"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ["BACKEND__DJANGO_SECRET_KEY"]

DEBUG = os.environ["ENVIRONMENT"].lower() in ["dev", "development"]

ALLOWED_HOSTS = os.environ["BACKEND__DJANGO_ALLOWED_HOSTS"].split(",")


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "account.apps.AccountConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "account.backend.AuthenticationBackend",
]

ROOT_URLCONF = "base.urls"

WSGI_APPLICATION = "base.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": os.environ["BACKEND__DJANGO_POSTGRES_DB_USER"],
        "PASSWORD": os.environ["BACKEND__DJANGO_POSTGRES_DB_PASSWORD"],
        "HOST": os.environ["BACKEND__DJANGO_POSTGRES_DB_HOST"],
        "PORT": int(os.environ["BACKEND__DJANGO_POSTGRES_DB_PORT"]),
        "NAME": os.environ["BACKEND__DJANGO_POSTGRES_DB_NAME"],
        "TIME_ZONE": os.environ["SERVER_TIMEZONE"],
    }
}


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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = os.environ["SERVER_TIMEZONE"]

USE_I18N = True

USE_TZ = True

# fmt: off
DATE_INPUT_FORMATS = [
    "%d-%m-%Y",     # '25-10-2006'
    "%d/%m/%Y",     # '25/10/2006'
    "%b %d %Y",     # 'Oct 25 2006'
    "%b %d, %Y",    # 'Oct 25, 2006'
    "%d %b %Y",     # '25 Oct 2006'
    "%d %b, %Y",    # '25 Oct, 2006'
    "%B %d %Y",     # 'October 25 2006'
    "%B %d, %Y",    # 'October 25, 2006'
    "%d %B %Y",     # '25 October 2006'
    "%d %B, %Y",    # '25 October, 2006'
]
# fmt: on

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "account.User"

CORS_ALLOWED_ORIGINS = os.environ["BACKEND__CORS_ALLOWED_ORIGINS"].split(",")
CORS_ALLOW_CREDENTIALS = True

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = os.environ["BACKEND__CSRF_TRUSTED_ORIGINS"].split(",")
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework_orjson.renderers.ORJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework_orjson.parsers.ORJSONParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    # Test Settings
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "TEST_REQUEST_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    # Encodings
    "UNICODE_JSON": False,
    "COERCE_DECIMAL_TO_STRING": False,
    # Other
    "UPLOADED_FILES_USE_URL": True,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(hours=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # custom
    "AUTH_COOKIE": "X-Authorization-Token",  # Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_SECURE": True,  # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag. It's not fetch by javascript.
    "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "AUTH_COOKIE_SAMESITE": "None",  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or 'None' to disable the flag; or None (python) to use the default (Lax)
    "REFRESH_COOKIE": "X-Refresh-Token",
    "REFRESH_COOKIE_DOMAIN": None,
    "REFRESH_COOKIE_SECURE": True,
    "REFRESH_COOKIE_HTTP_ONLY": True,
    "REFRESH_COOKIE_PATH": "/",
    "REFRESH_COOKIE_SAMESITE": "None",
}
