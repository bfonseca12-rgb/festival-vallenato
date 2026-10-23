from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_votaciones, name='lista_votaciones'),
    path('votar/<int:opcion_id>/', views.registrar_voto, name='registrar_voto'),
    path('registro/', views.registro, name='registro'),
]