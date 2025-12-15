from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def responder_pesquisa_view(request, ano):
    return HttpResponse(f"<h1>Pesquisa {ano}</h1><p>Em desenvolvimento...</p>")

@login_required
def minhas_pesquisas_view(request):
    return HttpResponse("<h1>Minhas Pesquisas</h1><p>Em desenvolvimento...</p>")