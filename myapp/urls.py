"""
este apartado para todas las urls que les pertene a esta app, para 
que el archvo de urls principal no se buelba muy complicado y tedioso de leer  
"""
#este es un ejemplo de como debe de funcionar.
from django.urls import path 
from . import views


urlpatterns = [

    path('', views.hello),

    path("prueba/", views.prueba)

]