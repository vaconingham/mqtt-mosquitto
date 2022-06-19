from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/client/(?P<client_name>\w+)/$', consumers.ClientConsumer.as_asgi()),
]