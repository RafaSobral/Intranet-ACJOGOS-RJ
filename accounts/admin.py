from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'nome_completo', 'tipo_usuario', 'email', 'ativo']
    list_filter = ['tipo_usuario', 'ativo', 'is_staff']
    search_fields = ['username', 'nome_completo', 'email', 'cpf']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'nome_completo', 'nome_social', 'cpf', 
                      'telefone', 'discord_nick')
        }),
        ('Endereço', {
            'fields': ('cep', 'endereco', 'numero', 'complemento', 
                      'bairro', 'cidade', 'estado')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )