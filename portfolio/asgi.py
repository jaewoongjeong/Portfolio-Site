"""
ASGI config for portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# It defines the channel URLs here!
'''
    - If there is a connection from the user, ProtocolTypeRouter() checks the connection's protocol, 
        then assigns to its corresponding Middleware
    - In this example, it gets connected to AuthMiddlewareStack(), where it restricts the users' scope
        based on their authentication success or failure
'''
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
