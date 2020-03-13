"""
ASGI config for roomy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from apps.client.views.notification import *
from django.core.asgi import get_asgi_application

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roomy.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/get_notif", notification),
    ])
})
