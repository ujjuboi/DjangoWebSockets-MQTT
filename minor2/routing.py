from django.urls import path, re_path    #for specifying path
from channels.routing import URLRouter, ProtocolTypeRouter  #for websocket protocol routing
from channels.auth import AuthMiddlewareStack   #authentication

#add consumers here
from graph.consumer import Graph
from firstpage.consumer import Firstpage
from secondPage.consumer import ChatConsumer

ws_pattern = [
    path('ws/home/', Firstpage.as_asgi()),
    path('ws/graph/', Graph.as_asgi()),
    re_path(r'ws/data/(?P<room_name>\w+)/(?P<auth_token>\S+)/$',ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(URLRouter(ws_pattern)),
    }
)