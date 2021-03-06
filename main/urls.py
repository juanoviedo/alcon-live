from django.urls import path
from . import views

urlpatterns = [

    path("enviarwsap/", views.enviarwsap, name="enviarwsap"),

    path("client/<int:id>/", views.client, name="client"),
    path("client/<int:id>/data/", views.data, name="data"),
    path("client/create/", views.create, name="create"),

    
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('avicultura/', views.avicultura, name="avicultura"),
    path('equinos/', views.equinos, name="equinos"),
    path('ganaderia/', views.ganaderia, name="ganaderia"),
    path('porcicultura/', views.porcicultura, name="porcicultura"),
    path('mascotas/', views.mascotas, name="mascotas"),
    path('cunicultura/', views.cunicultura, name="cunicultura"),
    path('acuicultura/', views.acuicultura, name="acuicultura"),
    path('vidinst/', views.vidinst, name="vidinst"),
    path('puntosventa/', views.puntosventa, name="puntosventa"),
    path('contactenos/', views.contactenos, name="contactenos"),
]