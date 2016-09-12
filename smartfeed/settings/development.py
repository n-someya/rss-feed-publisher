from smartfeed.settings.production import *

# SECURITY WARNING: don't run with debug turned on in production!

TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'tmp'))

DEBUG = True

SECRET = '42'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(TMP_PATH, 'db.sqlite3'),
                        }
                        }

INTERNAL_IPS = ('127.0.0.1',)



if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS += ('debug_toolbar',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

