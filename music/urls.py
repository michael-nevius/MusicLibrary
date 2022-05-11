from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_library),
    path('<int:pk>/', views.music_detail),
    path('<int:pk>/like/', views.like_song),
]