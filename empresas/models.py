from django.db import models
from django.conf import settings
from validate_docbr import CNPJ

class Empresa(models.Model):
    """
    Modelo de Empresa/Estúdio de jogos
    """
    
    PORTE_CHOICES = [
        ('MEI', 'Microempreendedor Individual'),
        ('ME', 'Microempresa'),
        ('EPP', 'Empresa de Pequeno Porte'),
        ('MEDIA', 'Média Empresa'),
        ('GRANDE', 'Grande Empresa'),
    ]
    
    # Dados Jurídicos
    nome_fantasia = models.CharField(max_length=200, verbose_name='Nome Fantasia')
    razao_social = models.CharField(max_length=200, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    porte = models.CharField(max_length=10, choices=PORTE_CHOICES, verbose_name='Porte')
    
    # Contato
    email = models.EmailField(verbose_name='E-mail de Contato')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    site = models.URLField(blank=True, verbose_name='Website')
    
    # Endereço
    cep = models.CharField(max_length=9, verbose_name='CEP')
    endereco = models.CharField(max_length=300, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=2, default='RJ', verbose_name='Estado')
    
    # Coordenadas para o mapa
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Relacionamentos
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='empresas_responsavel',
        verbose_name='Responsável'
    )
    
    membros = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='empresas_membro',
        blank=True,
        verbose_name='Membros da Equipe'
    )
    
    # Metadata
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    logo = models.ImageField(upload_to='empresas/logos/', blank=True, verbose_name='Logo')
    data_fundacao = models.DateField(null=True, blank=True, verbose_name='Data de Fundação')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativa = models.BooleanField(default=True)
    publica = models.BooleanField(default=True, verbose_name='Visível Publicamente')
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome_fantasia']
    
    def __str__(self):
        return self.nome_fantasia
    
    def clean(self):
        from django.core.exceptions import ValidationError
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(self.cnpj):
            raise ValidationError({'cnpj': 'CNPJ inválido'})