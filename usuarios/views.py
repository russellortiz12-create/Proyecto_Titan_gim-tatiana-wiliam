from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required  

# ==========================================
# VISTA DE REGISTRO DE NUEVOS USUARIOS
# ==========================================
def registro_view(request):
    """
    Función que gestiona el registro de nuevos aprendices o funcionarios en el sistema.
    """
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        confirmar = request.POST.get('confirmar_contrasena')
        
        # Validar si las contraseñas coinciden
        if contrasena != confirmar:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/registro.html')
            
        # Validar si el correo ya está registrado
        if User.objects.filter(email=correo).exists():
            messages.error(request, 'Ya existe una cuenta asociada a este correo institucional.')
            return render(request, 'usuarios/registro.html')
            
        try:
            # Creamos el usuario en el modelo nativo de Django (usamos el correo como username para mantener la consistencia)
            nuevo_usuario = User.objects.create_user(
                username=correo,
                email=correo,
                password=contrasena,
                first_name=nombres,
                last_name=apellidos
            )
            nuevo_usuario.save()
            
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Ocurrió un error al registrar: {e}')
            
    return render(request, 'usuarios/registro.html')


# ==========================================
# VISTA DE INICIO DE SESIÓN Y ENTRADA AL MÓDULO DE USUARIO
# ==========================================
def login_view(request):
    """
    Gestiona el acceso al sistema. Redirige a la vista del Módulo de Usuario 
    (aplica para aprendices, instructores y funcionarios) o al Módulo de Entrenador
    según la cuenta que inicie sesión.
    """
    if request.method == 'POST':
        correo_ingresado = request.POST.get('username')
        clave_ingresada = request.POST.get('password')
        
        try:
            # 1. Busca el usuario en la base de datos por su correo institucional
            usuario_encontrado = User.objects.get(email=correo_ingresado)
            
            # 2. Autentica las credenciales de la cuenta
            user = authenticate(request, username=usuario_encontrado.username, password=clave_ingresada)
            
            if user is not None:
                # 3. Registra el inicio de sesión exitoso
                login(request, user)
                
                # Correo asignado para el rol de Entrenador Principal
                correo_entrenador = "tatiana@soy.sena.edu.co" 
                
                # Validación de redirección por rol/correo
               # Validación de redirección por rol/correo
                if user.email == correo_entrenador:
                    return redirect('dashboard_entrenador')
                else:
                    return redirect('index_usuario')
            else:
                messages.error(request, 'La contraseña es incorrecta.')
                
        except User.DoesNotExist:
            messages.error(request, 'No existe ninguna cuenta registrada con este correo institucional.')
            
    return render(request, 'usuarios/login.html')

# ==========================================
# 1. VISTA DE INICIO (INDEX DEL USUARIO)
# ==========================================
@login_required(login_url='login')
def index_usuario_view(request):
    """
    Renderiza la vista principal del Módulo de Usuario.
    """
    correo_entrenador = "tatiana@soy.sena.edu.co"
    if request.user.email == correo_entrenador:
        return redirect('dashboard_entrenador')
        
    # Cambia 'usuarios/index.html' por 'usuarios/index_usuario.html'
    return render(request, 'usuarios/index_usuario.html')


# ==========================================
# 2. VISTA DE PERFIL DE USUARIO
# ==========================================
@login_required(login_url='login')
def perfil_usuario_view(request):
    """
    Renderiza la vista de perfil detallado del usuario (perfil_usuario.html),
    mostrando información personal, académica y de contacto.
    """
    return render(request, 'usuarios/perfil_usuario.html')


# ==========================================
# 3. VISTA DE RUTINAS DE ENTRENAMIENTO
# ==========================================
@login_required(login_url='login')
def rutina_usuario_view(request):
    """
    Renderiza la vista de rutinas asignadas al usuario (rutina_usuario.html),
    incluyendo calendario semanal y desglose de ejercicios.
    """
    return render(request, 'usuarios/rutina_usuario.html')


# ==========================================
# 4. VISTA DE PROGRESO Y MÉTRICAS
# ==========================================
@login_required(login_url='login')
def progreso_usuario_view(request):
    """
    Renderiza la vista de seguimiento físico y estadísticas (progreso_usuario.html)
    con gráficos de cumplimiento y racha de entrenamiento.
    """
    return render(request, 'usuarios/progreso_usuario.html')


# ==========================================
# 5. VISTA DE SUGERENCIAS Y FEEDBACK
# ==========================================
@login_required(login_url='login')
def sugerencias_usuario_view(request):
    """
    Renderiza la vista de buzón de sugerencias (sugerencias_usuario.html)
    para reportes de maquinaria, felicitaciones o comentarios de mejora.
    """
    return render(request, 'usuarios/sugerencias_usuario.html')