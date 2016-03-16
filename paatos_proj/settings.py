import os
from environ import Env

BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
assert os.path.exists(os.path.join(BASE_DIR, "manage.py"))

env = Env()

ALLOWED_HOSTS = ["*"]
DEBUG = True  # TODO
LANGUAGE_CODE = "en-us"
VAR_ROOT = env.str("VAR_ROOT", default=os.path.join(BASE_DIR, "var"))
if not os.path.isdir(VAR_ROOT):
    os.makedirs(VAR_ROOT)
MEDIA_ROOT = os.path.join(VAR_ROOT, "media")
MEDIA_URL = "/media/"
ROOT_URLCONF = "paatos_proj.urls"
SECRET_KEY = "paatos"  # TODO
STATIC_ROOT = os.path.join(VAR_ROOT, "static")
STATIC_URL = "/static/"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = "paatos_proj.wsgi.application"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "paatos"
]

MIDDLEWARE_CLASSES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

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

DATABASES = {
    "default": env.db_url(default="sqlite:///%s" % os.path.join(BASE_DIR, "db.sqlite3")),
}
