from django.urls import path
from main.consumers import DatapointUpdate

websocket_urlpatterns = [
    path('ws/dpupdate', DatapointUpdate),
]
