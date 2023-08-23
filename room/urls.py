from django.urls import path
from . import views
urlpatterns = [
    path('', views.rooms_view, name="rooms"),
    path('<slug:slug>/', views.room_view, name="room"),
]