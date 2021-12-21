release: python manage.py migrate --noinput --settings=config.settings.heroku
web: gunicorn config.wsgi --log-file - --log-level debug