from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_votaciones, name='lista_votaciones'),
    path('votar/<int:opcion_id>/', views.registrar_voto, name='registrar_voto'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='votaciones/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='lista_votaciones'), name='logout'),
]