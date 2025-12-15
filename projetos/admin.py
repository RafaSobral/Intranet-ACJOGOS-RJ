from django.contrib import admin
from .models import Projeto


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Projetos
    """
    list_display = [
        'nome',
        'empresa',
        'status',
        'genero',
        'data_lancamento',
        'publicado',
        'data_cadastro'
    ]
    
    list_filter = [
        'status',
        'genero',
        'publicado',
        'data_cadastro',
        'empresa'
    ]
    
    search_fields = [
        'nome',
        'descricao',
        'empresa__nome_fantasia'
    ]
    
    readonly_fields = [
        'data_cadastro',
        'data_atualizacao'
    ]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'empresa',
                'nome',
                'descricao',
                'status',
            )
        }),
        ('Classificação', {
            'fields': (
                'genero',
                'plataformas',
            )
        }),
        ('Mídia', {
            'fields': (
                'imagem_capa',
                'trailer_url',
            )
        }),
        ('Links', {
            'fields': (
                'link_steam',
                'link_play_store',
                'link_app_store',
                'link_itch',
                'link_site',
            ),
            'classes': ('collapse',)  # Deixa recolhido por padrão
        }),
        ('Datas', {
            'fields': (
                'data_inicio',
                'data_lancamento',
                'data_cadastro',
                'data_atualizacao',
            )
        }),
        ('Visibilidade', {
            'fields': (
                'publicado',
            )
        }),
    )
    
    date_hierarchy = 'data_cadastro'
    
    list_per_page = 25
    
    # Ações customizadas
    actions = ['publicar_projetos', 'despublicar_projetos']
    
    def publicar_projetos(self, request, queryset):
        """Publica os projetos selecionados"""
        updated = queryset.update(publicado=True)
        self.message_user(request, f'{updated} projeto(s) publicado(s) com sucesso.')
    publicar_projetos.short_description = "Publicar projetos selecionados"
    
    def despublicar_projetos(self, request, queryset):
        """Despublica os projetos selecionados"""
        updated = queryset.update(publicado=False)
        self.message_user(request, f'{updated} projeto(s) despublicado(s) com sucesso.')
    despublicar_projetos.short_description = "Despublicar projetos selecionados"