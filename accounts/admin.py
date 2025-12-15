from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Configuração do admin para Usuários customizados
    """
    list_display = [
        'username',
        'nome_completo',
        'email',
        'tipo_usuario',
        'cidade',
        'ativo',
        'is_staff',
        'data_cadastro'
    ]
    
    list_filter = [
        'tipo_usuario',
        'ativo',
        'is_staff',
        'is_superuser',
        'cidade',
        'estado',
        'data_cadastro'
    ]
    
    search_fields = [
        'username',
        'nome_completo',
        'email',
        'cpf',
        'telefone'
    ]
    
    readonly_fields = [
        'date_joined',
        'last_login',
        'data_cadastro',
        'data_atualizacao'
    ]
    
    # Customização dos fieldsets do UserAdmin padrão
    fieldsets = (
        ('Credenciais', {
            'fields': ('username', 'password')
        }),
        ('Informações Pessoais', {
            'fields': (
                'nome_completo',
                'nome_social',
                'email',
                'cpf',
                'telefone',
                'discord_nick',
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
        ('Tipo e Permissões', {
            'fields': (
                'tipo_usuario',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Status', {
            'fields': (
                'ativo',
                'date_joined',
                'last_login',
                'data_cadastro',
                'data_atualizacao',
            )
        }),
    )
    
    # Fieldsets para criação de novo usuário
    add_fieldsets = (
        ('Credenciais', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Informações Básicas', {
            'classes': ('wide',),
            'fields': (
                'nome_completo',
                'cpf',
                'telefone',
                'tipo_usuario',
            ),
        }),
        ('Endereço', {
            'classes': ('wide', 'collapse'),
            'fields': (
                'cep',
                'endereco',
                'numero',
                'bairro',
                'cidade',
            ),
        }),
    )
    
    date_hierarchy = 'data_cadastro'
    
    list_per_page = 25
    
    ordering = ['-data_cadastro']
    
    # Ações customizadas
    actions = ['ativar_usuarios', 'desativar_usuarios', 'promover_para_associado', 'promover_para_diretoria']
    
    def ativar_usuarios(self, request, queryset):
        """Ativa os usuários selecionados"""
        updated = queryset.update(ativo=True, is_active=True)
        self.message_user(request, f'{updated} usuário(s) ativado(s) com sucesso.')
    ativar_usuarios.short_description = "Ativar usuários selecionados"
    
    def desativar_usuarios(self, request, queryset):
        """Desativa os usuários selecionados"""
        updated = queryset.update(ativo=False, is_active=False)
        self.message_user(request, f'{updated} usuário(s) desativado(s) com sucesso.')
    desativar_usuarios.short_description = "Desativar usuários selecionados"
    
    def promover_para_associado(self, request, queryset):
        """Promove afiliados para associados"""
        updated = queryset.filter(tipo_usuario='afiliado').update(tipo_usuario='associado')
        self.message_user(request, f'{updated} usuário(s) promovido(s) para Associado.')
    promover_para_associado.short_description = "Promover para Associado"
    
    def promover_para_diretoria(self, request, queryset):
        """Promove para diretoria"""
        updated = queryset.update(tipo_usuario='diretoria')
        self.message_user(request, f'{updated} usuário(s) promovido(s) para Diretoria.')
    promover_para_diretoria.short_description = "Promover para Diretoria"