from django.contrib.auth.models import AbstractUser
from django.db import models
from validate_docbr import CPF

class Usuario(AbstractUser):
    """
    Modelo de usuário customizado para a Intranet ACJOGOS-RJ
    """
    
    TIPO_USUARIO_CHOICES = [
        ('diretoria', 'Diretoria'),
        ('associado', 'Associado'),
        ('afiliado', 'Afiliado'),
        ('coletivo', 'Coletivo/Institucional'),
    ]
    
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPO_USUARIO_CHOICES,
        default='afiliado',
        verbose_name='Tipo de Usuário'
    )
    
    nome_completo = models.CharField(max_length=200, verbose_name='Nome Completo')
    nome_social = models.CharField(max_length=200, blank=True, verbose_name='Nome Social')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    discord_nick = models.CharField(max_length=100, blank=True, verbose_name='Nick no Discord')
    
    # Endereço
    cep = models.CharField(max_length=9, verbose_name='CEP')
    endereco = models.CharField(max_length=300, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=2, default='RJ', verbose_name='Estado')
    
    # Metadata
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome_completo']
    
    def __str__(self):
        return f"{self.nome_completo} ({self.get_tipo_usuario_display()})"
    
    def is_diretoria(self):
        return self.tipo_usuario == 'diretoria'
    
    def is_associado(self):
        return self.tipo_usuario == 'associado'
    
    def is_afiliado(self):
        return self.tipo_usuario == 'afiliado'
    
    def clean(self):
        from django.core.exceptions import ValidationError
        cpf_validator = CPF()
        if not cpf_validator.validate(self.cpf):
            raise ValidationError({'cpf': 'CPF inválido'})