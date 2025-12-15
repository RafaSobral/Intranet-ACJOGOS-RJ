from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Empresas
    """
    list_display = [
        'nome_fantasia',
        'cnpj',
        'cidade',
        'porte',
        'responsavel',
        'ativa',
        'publica',
        'data_cadastro'
    ]
    
    list_filter = [
        'ativa',
        'publica',
        'cidade',
        'porte',
        'estado',
        'data_cadastro'
    ]
    
    search_fields = [
        'nome_fantasia',
        'razao_social',
        'cnpj',
        'email',
        'responsavel__nome_completo'
    ]
    
    readonly_fields = [
        'data_cadastro',
        'data_atualizacao'
    ]
    
    filter_horizontal = ['membros']  # Interface melhor para ManyToMany
    
    fieldsets = (
        ('Dados Jurídicos', {
            'fields': (
                'nome_fantasia',
                'razao_social',
                'cnpj',
                'porte',
            )
        }),
        ('Contato', {
            'fields': (
                'email',
                'telefone',
                'site',
            )
        }),
        ('Endereço', {
            'fields': (
                'cep',
                'endereco',
                'numero',
                'complemento',
                'bairro',
                'cidade',
                'estado',
            )
        }),
        ('Coordenadas (Mapa)', {
            'fields': (
                'latitude',
                'longitude',
            ),
            'classes': ('collapse',)
        }),
        ('Relacionamentos', {
            'fields': (
                'responsavel',
                'membros',
            )
        }),
        ('Informações Adicionais', {
            'fields': (
                'descricao',
                'logo',
                'data_fundacao',
            )
        }),
        ('Status', {
            'fields': (
                'ativa',
                'publica',
                'data_cadastro',
                'data_atualizacao',
            )
        }),
    )
    
    date_hierarchy = 'data_cadastro'
    
    list_per_page = 25
    
    # Ações customizadas
    actions = ['ativar_empresas', 'desativar_empresas', 'tornar_publicas', 'tornar_privadas']
    
    def ativar_empresas(self, request, queryset):
        """Ativa as empresas selecionadas"""
        updated = queryset.update(ativa=True)
        self.message_user(request, f'{updated} empresa(s) ativada(s) com sucesso.')
    ativar_empresas.short_description = "Ativar empresas selecionadas"
    
    def desativar_empresas(self, request, queryset):
        """Desativa as empresas selecionadas"""
        updated = queryset.update(ativa=False)
        self.message_user(request, f'{updated} empresa(s) desativada(s) com sucesso.')
    desativar_empresas.short_description = "Desativar empresas selecionadas"
    
    def tornar_publicas(self, request, queryset):
        """Torna as empresas visíveis publicamente"""
        updated = queryset.update(publica=True)
        self.message_user(request, f'{updated} empresa(s) tornada(s) pública(s) com sucesso.')
    tornar_publicas.short_description = "Tornar públicas"
    
    def tornar_privadas(self, request, queryset):
        """Torna as empresas privadas"""
        updated = queryset.update(publica=False)
        self.message_user(request, f'{updated} empresa(s) tornada(s) privada(s) com sucesso.')
    tornar_privadas.short_description = "Tornar privadas"
    
    def get_queryset(self, request):
        """
        Otimiza queries com select_related
        """
        qs = super().get_queryset(request)
        return qs.select_related('responsavel').prefetch_related('membros')