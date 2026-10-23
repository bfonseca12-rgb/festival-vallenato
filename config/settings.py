import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ... (MANTIENE AQUÍ TU SECRET_KEY, DEBUG, ALLOWED_HOSTS Y INSTALLED_APPS) ...

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- WhiteNoise para servir archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... (MANTIENE AQUÍ ROOT_URLCONF, TEMPLATES, WSGI_APPLICATION, DATABASES, ETC.) ...

# Configuración de Archivos Estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'

# Carpeta donde Django recopilará todos los estáticos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Carpetas donde Django buscará archivos estáticos locales
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'votaciones' / 'static',
]

# Almacenamiento optimizado y comprimido con WhiteNoise para Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'