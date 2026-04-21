from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from usuarios.forms import CreacionUsuario
from django.contrib.auth.decorators import login_required

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            
            login(request,user)
            
            return redirect("viajes_app:inicio")
    
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'usuarios/iniciar_sesion.html',{'formulario_iniciar_sesion': formulario})

def registrarse(request):
    
    if request.method == "POST":
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:iniciar_sesion")
    else:
        formulario = CreacionUsuario()
        
    return render(request, 'usuarios/registro.html', {'formulario_registro': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')