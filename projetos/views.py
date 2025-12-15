from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def meus_projetos_view(request):
    return HttpResponse("<h1>Meus Projetos</h1><p>Em desenvolvimento...</p>")

@login_required
def criar_projeto_view(request):
    return HttpResponse("<h1>Criar Projeto</h1><p>Em desenvolvimento...</p>")

@login_required
def visualizar_projeto_view(request, pk):
    return HttpResponse(f"<h1>Projeto #{pk}</h1><p>Em desenvolvimento...</p>")

@login_required
def editar_projeto_view(request, pk):
    return HttpResponse(f"<h1>Editar Projeto #{pk}</h1><p>Em desenvolvimento...</p>")

@login_required
def deletar_projeto_view(request, pk):
    return HttpResponse(f"<h1>Deletar Projeto #{pk}</h1><p>Em desenvolvimento...</p>")