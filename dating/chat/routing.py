from django.urls import path
from .consumers import ChatroomConsumer

websocket_urlpatterns = [
    path('ws/chat/<group_name>/', ChatroomConsumer.as_asgi()),
    
]
