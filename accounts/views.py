from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def registro_view(request):
    return HttpResponse("<h1>Página de Registro</h1><p>Em desenvolvimento...</p>")

def login_view(request):
    return HttpResponse("<h1>Página de Login</h1><p>Em desenvolvimento...</p>")

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('publico:home')

@login_required
def dashboard_view(request):
    return HttpResponse(f"<h1>Dashboard</h1><p>Bem-vindo, {request.user.username}!</p>")

@login_required
def perfil_view(request):
    return HttpResponse(f"<h1>Perfil</h1><p>{request.user.username}</p>")

@login_required
def editar_perfil_view(request):
    return HttpResponse("<h1>Editar Perfil</h1><p>Em desenvolvimento...</p>")