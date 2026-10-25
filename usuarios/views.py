from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    """
    Vista principal de bienvenida pública.
    """
    return render(request, 'usuarios/index.html')

@login_required(login_url='/admin/login/')
def dashboard(request):
    usuario_actual = request.user
    es_admin_o_instructor = usuario_actual.is_staff or usuario_actual.is_superuser
    
    contexto = {
        'usuario': usuario_actual,
        'es_instructor': es_admin_o_instructor,
    }
    
    # Cambiamos 'contextO' por 'context'
    return render(request, 'usuarios/dashboard.html', context=contexto)