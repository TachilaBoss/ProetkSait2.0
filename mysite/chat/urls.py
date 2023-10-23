from django.urls import path
from. import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('', views.home, name='home/'),
    path('chat/<str:room_name>/', views.room, name='room/'),
    path('add_message/', views.add_message, name='add_message/'),
    path('messages/', views.message_list, name='message_list/'),
    path('add_message/<str:room_name>/', views.add_message, name='add_message/'),
]
