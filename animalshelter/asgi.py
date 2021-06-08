"""
ASGI config for animalshelter project.

It exposes the ASGI callable as a module-level variable named ``applianimalion``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_applianimalion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animalshelter.settings')

applianimalion = get_asgi_applianimalion()
