SECRET_KEY = 'django-insecure-robomunch-backend-cloud-key-2026'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'app',
]
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]
ROOT_URLCONF = 'backend.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
