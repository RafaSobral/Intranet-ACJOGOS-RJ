from django.db import models
from django.conf import settings
from empresas.models import Empresa

class PesquisaAnual(models.Model):
    """
    Modelo para armazenar dados da pesquisa socioeconômica anual
    """
    
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='pesquisas',
        verbose_name='Empresa'
    )
    ano = models.IntegerField(verbose_name='Ano da Pesquisa')
    
    # Dados Econômicos
    faturamento_anual = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        verbose_name='Faturamento Anual (R$)'
    )
    numero_funcionarios = models.IntegerField(verbose_name='Número de Funcionários')
    numero_projetos_ativos = models.IntegerField(verbose_name='Projetos Ativos')
    numero_projetos_lancados = models.IntegerField(verbose_name='Projetos Lançados no Ano')
    
    # Investimentos
    investimento_desenvolvimento = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Investimento em Desenvolvimento (R$)'
    )
    investimento_marketing = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Investimento em Marketing (R$)'
    )
    
    # Mercado
    mercado_principal = models.CharField(
        max_length=50,
        choices=[
            ('nacional', 'Nacional'),
            ('internacional', 'Internacional'),
            ('ambos', 'Ambos')
        ],
        verbose_name='Mercado Principal'
    )
    
    # Desafios e Expectativas
    principais_desafios = models.TextField(verbose_name='Principais Desafios')
    expectativas_proximo_ano = models.TextField(verbose_name='Expectativas para o Próximo Ano')
    
    # Metadata
    data_preenchimento = models.DateTimeField(auto_now_add=True)
    preenchido_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Preenchido por'
    )
    
    class Meta:
        verbose_name = 'Pesquisa Anual'
        verbose_name_plural = 'Pesquisas Anuais'
        unique_together = ['empresa', 'ano']
        ordering = ['-ano', 'empresa']
    
    def __str__(self):
        return f"Pesquisa {self.ano} - {self.empresa.nome_fantasia}"