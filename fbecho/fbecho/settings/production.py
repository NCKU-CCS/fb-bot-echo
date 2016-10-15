import json
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Secret key
with open(".secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """Get the enviroment variable or return exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} enviroment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

VERIFICATION_CODE = get_secret('verification_code')
FB_TOKEN = get_secret('FB_TOKEN')
