"""
ASGI config for roomy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from apps.core.roomy_core.views.consumers import *
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roomy.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notif-channel/booking/", booking_notif),
    ])
})
