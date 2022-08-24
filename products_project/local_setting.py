# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iac52jo+i!=)8jy%aal91!@w9zut)-%w(^(pe%6&zdr&4d+9s9'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}