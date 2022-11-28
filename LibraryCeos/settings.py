import os
import django_on_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dn4!q!tvvyh7qy$wf**l7j#i^th-nd#%nul=3$kp+!59c%&=@!'
#SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

#RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
#if RENDER_EXTERNAL_HOSTNAME:    
#    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #providers
    'allauth.socialaccount.providers.google',
    
    # 'nomedoapp.apps.NomedoappConfig',
    'core.apps.CoreConfig',
    'cadastros.apps.CadastrosConfig',
    'usuarios.apps.UsuariosConfig',
    'chat.apps.ChatConfig',
    
    'django_cleanup.apps.CleanupConfig',
    'crispy_forms',
    'django_filters',
    'channels',
]

#SITE_ID = 1

#Crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryCeos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryCeos.wsgi.application'
ASGI_APPLICATION = 'LibraryCeos.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': dj_database_url.config(default='postgresql://postgres:postgres@localhost:5432/libraryceos', conn_max_age=600)}

#AUTHENTICATION_BACKENDS = [

#    'django.contrib.auth.backends.ModelBackend',

    
#    'allauth.account.auth_backends.AuthenticationBackend',
#]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#STATIC_URL = '/static/'
#if not DEBUG:    #
#    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static")
#]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Arquivos > Uploads
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/uploads/" #Visualizar imagens

#Configurações de Autenticação
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

django_on_heroku.settings(locals())
