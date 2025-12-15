from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def minhas_empresas_view(request):
    return HttpResponse("<h1>Minhas Empresas</h1><p>Em desenvolvimento...</p>")

@login_required
def criar_empresa_view(request):
    return HttpResponse("<h1>Criar Empresa</h1><p>Em desenvolvimento...</p>")

@login_required
def visualizar_empresa_view(request, pk):
    return HttpResponse(f"<h1>Empresa #{pk}</h1><p>Em desenvolvimento...</p>")

@login_required
def editar_empresa_view(request, pk):
    return HttpResponse(f"<h1>Editar Empresa #{pk}</h1><p>Em desenvolvimento...</p>")

@login_required
def deletar_empresa_view(request, pk):
    return HttpResponse(f"<h1>Deletar Empresa #{pk}</h1><p>Em desenvolvimento...</p>")

@login_required
def gerenciar_membros_view(request, pk):
    return HttpResponse(f"<h1>Gerenciar Membros - Empresa #{pk}</h1><p>Em desenvolvimento...</p>")