from django.db import models
from empresas.models import Empresa

class Projeto(models.Model):
    """
    Modelo de Projeto de Jogo
    """
    
    STATUS_CHOICES = [
        ('conceito', 'Em Conceito'),
        ('desenvolvimento', 'Em Desenvolvimento'),
        ('prototipo', 'Protótipo'),
        ('beta', 'Beta/Testes'),
        ('lancado', 'Lançado'),
        ('cancelado', 'Cancelado'),
    ]
    
    PLATAFORMA_CHOICES = [
        ('pc', 'PC'),
        ('mobile', 'Mobile'),
        ('console', 'Console'),
        ('web', 'Web Browser'),
        ('vr', 'VR/AR'),
    ]
    
    GENERO_CHOICES = [
        ('acao', 'Ação'),
        ('aventura', 'Aventura'),
        ('rpg', 'RPG'),
        ('estrategia', 'Estratégia'),
        ('puzzle', 'Puzzle'),
        ('simulacao', 'Simulação'),
        ('esporte', 'Esporte'),
        ('corrida', 'Corrida'),
        ('educativo', 'Educativo'),
        ('casual', 'Casual'),
        ('outros', 'Outros'),
    ]
    
    # Dados básicos
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        related_name='projetos',
        verbose_name='Empresa'
    )
    nome = models.CharField(max_length=200, verbose_name='Nome do Projeto')
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    
    # Classificação
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, verbose_name='Gênero')
    plataformas = models.CharField(max_length=200, verbose_name='Plataformas')
    
    # Mídia
    imagem_capa = models.ImageField(upload_to='projetos/capas/', blank=True, verbose_name='Imagem de Capa')
    trailer_url = models.URLField(blank=True, verbose_name='URL do Trailer')
    
    # Links
    link_steam = models.URLField(blank=True, verbose_name='Link Steam')
    link_play_store = models.URLField(blank=True, verbose_name='Link Play Store')
    link_app_store = models.URLField(blank=True, verbose_name='Link App Store')
    link_itch = models.URLField(blank=True, verbose_name='Link Itch.io')
    link_site = models.URLField(blank=True, verbose_name='Website do Jogo')
    
    # Datas
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data de Início')
    data_lancamento = models.DateField(null=True, blank=True, verbose_name='Data de Lançamento')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Visibilidade
    publicado = models.BooleanField(default=True, verbose_name='Visível Publicamente')
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return f"{self.nome} - {self.empresa.nome_fantasia}"