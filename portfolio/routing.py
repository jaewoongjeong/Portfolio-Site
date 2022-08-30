from django.urls import re_path

from . import consumers

# It contains all the URL patterns for the websocket
websocket_urlpatterns = [
    re_path(r'ws/crypto/details/$', consumers.ChatConsumer.as_asgi()),
]