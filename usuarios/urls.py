from django.urls import path
from .views import login_view

urlpatterns = [
    path('', login_view, name='login'), # Al entrar a la raíz, muestra el login
]