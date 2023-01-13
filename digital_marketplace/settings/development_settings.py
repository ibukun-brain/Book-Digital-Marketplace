from .base_settings import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
] 


INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = 'assets/'
STATICFILES_DIRS = [
    BASE_DIR / 'assets'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static_cdn'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

