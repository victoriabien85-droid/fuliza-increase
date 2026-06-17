import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the Django application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fuliza_updatess.settings')

# Expose the WSGI application object for Gunicorn (app:app).
app = get_wsgi_application()
