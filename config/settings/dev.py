import os

from .base import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Use SQLite for development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

# Security settings
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "your-secret-key-for-dev")
