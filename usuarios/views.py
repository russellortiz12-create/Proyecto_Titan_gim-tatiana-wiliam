from django.shortcuts import render

def login_view(request):
    # Esta función le ordena a Django buscar y renderizar tu login real
    return render(request, 'usuarios/login.html')