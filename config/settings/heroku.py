from .base import *
import django_heroku
# Activate Django-Heroku.
django_heroku.settings(locals())
DEBUG = True