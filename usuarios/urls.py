from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la Portada / Landing Page (Página principal del sitio)
    path('', views.principal_view, name='principal'),
    
    # Rutas de Autenticación
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    
    # Rutas del Módulo de Usuario (Navegación del Sidebar)
    path('inicio/', views.index_usuario_view, name='index_usuario'),
    path('perfil/', views.perfil_usuario_view, name='perfil_usuario'),
    path('rutina/', views.rutina_usuario_view, name='rutina_usuario'),
    path('progreso/', views.progreso_usuario_view, name='progreso_usuario'),
    path('sugerencias/', views.sugerencias_usuario_view, name='sugerencias_usuario'),
]