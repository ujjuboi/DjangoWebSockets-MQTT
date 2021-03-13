from django.urls import path    #for specifying path
from channels.routing import URLRouter, ProtocolTypeRouter  #for websocket protocol routing
from channels.auth import AuthMiddlewareStack   #authentication

#add consumers here
from graph.consumer import Graph
from firstpage.consumer import Firstpage

ws_pattern = [
    path('ws/home/', Firstpage.as_asgi()),
    path('ws/graph/', Graph.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(URLRouter(ws_pattern)),
    }
)