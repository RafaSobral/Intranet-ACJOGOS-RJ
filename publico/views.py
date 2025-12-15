from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """Página inicial - versão temporária"""
    return HttpResponse("<h1>Bem-vindo à ACJOGOS-RJ!</h1><p>Sistema em desenvolvimento...</p>")

def empresas_list_view(request):
    """Lista de empresas - versão temporária"""
    return HttpResponse("<h1>Lista de Empresas</h1><p>Em breve...</p>")

def projetos_list_view(request):
    """Lista de projetos - versão temporária"""
    return HttpResponse("<h1>Lista de Projetos</h1><p>Em breve...</p>")

def mapa_view(request):
    """Mapa interativo - versão temporária"""
    return HttpResponse("<h1>Mapa de Empresas</h1><p>Em breve...</p>")

def empresa_detail_view(request, pk):
    """Detalhes de empresa - versão temporária"""
    return HttpResponse(f"<h1>Empresa #{pk}</h1><p>Em breve...</p>")

def projeto_detail_view(request, pk):
    """Detalhes de projeto - versão temporária"""
    return HttpResponse(f"<h1>Projeto #{pk}</h1><p>Em breve...</p>")

def empresas_mapa_json(request):
    """API JSON para o mapa - versão temporária"""
    from django.http import JsonResponse
    return JsonResponse({'empresas': []})