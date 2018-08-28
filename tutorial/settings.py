import os

# region Paths

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# endregion

# region Urls

ROOT_URLCONF = "tutorial.urls"
STATIC_URL = "/static/"

# endregion

# region Application definition

INSTALLED_APPS = [

    # region Django

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django_extensions",

    # endregion

    # region REST

    "rest_framework",

    # endregion
]

INSTALLED_APPS += [
    "tutorial.quickstart",
    "tutorial.snippets",
]

# endregion

# region Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# endregion

# region Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# endregion

# region Password validation.

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# endregion

# region Miscellaneous

WSGI_APPLICATION = "tutorial.wsgi.application"

# endregion

# region Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# endregion

# region Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# endregion

SECRET_KEY = "dtd@!*&f&nwa(wj^y3)yp5z7%2jlc=)kn463wq#&htdbx(r6y2"

# region Debug

DEBUG = True
ALLOWED_HOSTS = ["*"]

# endregion
