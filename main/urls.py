from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ganado/', views.ganado, name="ganado"),
]