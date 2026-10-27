from django.urls import path #<-- importa funcion desde las librerias de Django
from .views import login_view
"""Importa la función login_view que creamos en el archivo 
views.py de la carpeta actual (el punto . significa aquí mismo)."""

urlpatterns = [
    path('', login_view, name='login'), # Al entrar a la raíz, muestra el login
]