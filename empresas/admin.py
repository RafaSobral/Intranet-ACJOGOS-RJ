from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome_fantasia', 'cnpj', 'cidade', 'responsavel', 'ativa']
    list_filter = ['ativa', 'cidade', 'porte']
    search_fields = ['nome_fantasia', 'cnpj']