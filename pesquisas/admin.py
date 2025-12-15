from django.contrib import admin
from .models import PesquisaAnual


@admin.register(PesquisaAnual)
class PesquisaAnualAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Pesquisas Anuais
    """
    list_display = [
        'empresa',
        'ano',
        'faturamento_anual',
        'numero_funcionarios',
        'numero_projetos_ativos',
        'mercado_principal',
        'data_preenchimento'
    ]
    
    list_filter = [
        'ano',
        'mercado_principal',
        'data_preenchimento',
        'empresa__cidade'
    ]
    
    search_fields = [
        'empresa__nome_fantasia',
        'empresa__razao_social'
    ]
    
    readonly_fields = [
        'data_preenchimento',
        'preenchido_por'
    ]
    
    fieldsets = (
        ('Identificação', {
            'fields': (
                'empresa',
                'ano',
                'preenchido_por',
                'data_preenchimento',
            )
        }),
        ('Dados Econômicos', {
            'fields': (
                'faturamento_anual',
                'numero_funcionarios',
                'numero_projetos_ativos',
                'numero_projetos_lancados',
            )
        }),
        ('Investimentos', {
            'fields': (
                'investimento_desenvolvimento',
                'investimento_marketing',
            )
        }),
        ('Mercado', {
            'fields': (
                'mercado_principal',
            )
        }),
        ('Desafios e Expectativas', {
            'fields': (
                'principais_desafios',
                'expectativas_proximo_ano',
            ),
            'classes': ('collapse',)
        }),
    )
    
    date_hierarchy = 'data_preenchimento'
    
    list_per_page = 25
    
    ordering = ['-ano', 'empresa']
    
    actions = ['exportar_para_excel']
    
    def exportar_para_excel(self, request, queryset):
        """
        Exporta as pesquisas selecionadas para Excel
        """
        self.message_user(
            request, 
            f'{queryset.count()} pesquisa(s) selecionada(s). Funcionalidade de exportação será implementada em breve.'
        )
    exportar_para_excel.short_description = "Exportar para Excel"
    
    def get_queryset(self, request):
        """
        Customiza o queryset para otimizar queries
        """
        qs = super().get_queryset(request)
        return qs.select_related('empresa', 'preenchido_por')
    
    def save_model(self, request, obj, form, change):
        """
        Salva o modelo e adiciona o usuário que preencheu
        """
        if not obj.preenchido_por:
            obj.preenchido_por = request.user
        super().save_model(request, obj, form, change)