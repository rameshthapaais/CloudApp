"""
ASGI config for greatkart project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings_module = 'greatkart.production' if 'WEBSITE_HOSTNAME' in os.environ else 'greatkart.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greatkart.settings')

application = get_asgi_application()
