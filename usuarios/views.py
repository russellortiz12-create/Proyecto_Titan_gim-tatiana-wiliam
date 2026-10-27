from django.shortcuts import render #<-- Exporta una herramienta que ya viene incluida en Django
                                                            #<-- llamada render
"""Es la función encargada de unir la lógica 
de Python con nuestra plantilla visual HTML 
para enviársela al navegador web."""

def login_view(request): #<-- Define y crea una nueva funcion en python
    # Esta función le ordena a Django buscar y renderizar tu login real
    return render(request, 'usuarios/login.html')

"""Es la orden final de la vista: le indica a Django que renderice 
(pinte en pantalla) nuestra interfaz gráfica del login"""