from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Count
from empresas.models import Empresa
from projetos.models import Projeto


def home_view(request):
    """
    Página inicial pública
    """
    # Estatísticas gerais
    total_empresas = Empresa.objects.filter(ativa=True, publica=True).count()
    total_projetos = Projeto.objects.filter(publicado=True).count()
    
    # Empresas em destaque (últimas cadastradas)
    empresas_destaque = Empresa.objects.filter(
        ativa=True, 
        publica=True
    ).order_by('-data_cadastro')[:6]
    
    # Projetos em destaque
    projetos_destaque = Projeto.objects.filter(
        publicado=True
    ).order_by('-data_cadastro')[:6]
    
    context = {
        'total_empresas': total_empresas,
        'total_projetos': total_projetos,
        'empresas_destaque': empresas_destaque,
        'projetos_destaque': projetos_destaque,
    }
    
    return render(request, 'publico/home.html', context)


def empresas_list_view(request):
    """
    Listagem pública de empresas com filtros
    """
    empresas = Empresa.objects.filter(ativa=True, publica=True)
    
    # Filtros
    cidade = request.GET.get('cidade')
    porte = request.GET.get('porte')
    busca = request.GET.get('busca')
    
    if cidade:
        empresas = empresas.filter(cidade__icontains=cidade)
    
    if porte:
        empresas = empresas.filter(porte=porte)
    
    if busca:
        empresas = empresas.filter(
            Q(nome_fantasia__icontains=busca) | 
            Q(descricao__icontains=busca)
        )
    
    # Anotações
    empresas = empresas.annotate(
        total_projetos=Count('projetos')
    )
    
    # Lista de cidades para filtro
    cidades = Empresa.objects.filter(
        ativa=True, 
        publica=True
    ).values_list('cidade', flat=True).distinct().order_by('cidade')
    
    context = {
        'empresas': empresas,
        'cidades': cidades,
        'cidade_selecionada': cidade,
        'porte_selecionado': porte,
        'busca': busca,
    }
    
    return render(request, 'publico/empresas_list.html', context)


def empresa_detail_view(request, pk):
    """
    Detalhes de uma empresa específica
    """
    empresa = get_object_or_404(
        Empresa, 
        pk=pk, 
        ativa=True, 
        publica=True
    )
    
    # Projetos da empresa
    projetos = empresa.projetos.filter(publicado=True)
    
    context = {
        'empresa': empresa,
        'projetos': projetos,
    }
    
    return render(request, 'publico/empresa_detail.html', context)


def projetos_list_view(request):
    """
    Listagem pública de projetos com filtros
    """
    projetos = Projeto.objects.filter(publicado=True).select_related('empresa')
    
    # Filtros
    status = request.GET.get('status')
    genero = request.GET.get('genero')
    busca = request.GET.get('busca')
    
    if status:
        projetos = projetos.filter(status=status)
    
    if genero:
        projetos = projetos.filter(genero=genero)
    
    if busca:
        projetos = projetos.filter(
            Q(nome__icontains=busca) | 
            Q(descricao__icontains=busca)
        )
    
    context = {
        'projetos': projetos,
        'status_selecionado': status,
        'genero_selecionado': genero,
        'busca': busca,
        'status_choices': Projeto.STATUS_CHOICES,
        'genero_choices': Projeto.GENERO_CHOICES,
    }
    
    return render(request, 'publico/projetos_list.html', context)


def projeto_detail_view(request, pk):
    """
    Detalhes de um projeto específico
    """
    projeto = get_object_or_404(
        Projeto, 
        pk=pk, 
        publicado=True
    )
    
    # Outros projetos da mesma empresa
    projetos_relacionados = Projeto.objects.filter(
        empresa=projeto.empresa,
        publicado=True
    ).exclude(pk=pk)[:4]
    
    context = {
        'projeto': projeto,
        'projetos_relacionados': projetos_relacionados,
    }
    
    return render(request, 'publico/projeto_detail.html', context)


def mapa_view(request):
    """
    Página do mapa interativo de empresas
    """
    return render(request, 'publico/mapa.html')


def empresas_mapa_json(request):
    """
    API JSON para retornar dados das empresas para o mapa
    """
    empresas = Empresa.objects.filter(
        ativa=True,
        publica=True,
        latitude__isnull=False,
        longitude__isnull=False
    ).values(
        'id',
        'nome_fantasia',
        'cidade',
        'latitude',
        'longitude',
        'site'
    )
    
    data = {
        'empresas': list(empresas)
    }
    
    return JsonResponse(data)