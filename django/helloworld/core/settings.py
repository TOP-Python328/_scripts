"""
Django settings for helloworld project.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


WSGI_APPLICATION = 'core.wsgi.application'

SECRET_KEY = 'django-insecure-f1cd7j$u_+4tlb6z8-wbaj+jgjvn*c71(a1gyjs_sc9_!8*=3o'

DEBUG = True

ALLOWED_HOSTS = []
ROOT_URLCONF = 'core.urls'


INSTALLED_APPS = [
    'first',
]

TIME_ZONE = 'Asia/Yekaterinburg'
USE_TZ = True
