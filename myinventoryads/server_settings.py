from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = '_&8sv%o^883*r$+)-$5gfdg5346bm+k-4qz+e!3a79e$!c6=nv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['inventoryads.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'da2ocg30uggmgc',
        'USER': 'zeyaoufzhreotp',
        'PASSWORD': '1040fce340de8ca47c1c8aea45a43f708986091eec9a4781ab9d79bca7bf76c4',
        'HOST': 'ec2-18-210-214-86.compute-1.amazonaws.com',
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'myinventoryads/static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

