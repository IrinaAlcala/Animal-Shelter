"""
WSGI config for animalshelter project.

It exposes the WSGI callable as a module-level variable named ``applianimalion``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_applianimalion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animalshelter.settings')

applianimalion = get_wsgi_applianimalion()
