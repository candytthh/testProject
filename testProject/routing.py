from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import main.routing
# from .consumers import DatapointUpdate


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            main.routing.websocket_urlpatterns

        )
    ),
})
