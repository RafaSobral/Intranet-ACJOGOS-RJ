from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from validate_docbr import CPF


class UsuarioRegistroForm(UserCreationForm):
    """
    Formulário de registro de novo usuário
    """
    
    nome_completo = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome completo'
        })
    )
    
    nome_social = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome social (opcional)'
        })
    )
    
    cpf = forms.CharField(
        max_length=14,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00',
            'data-mask': '000.000.000-00'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    
    telefone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(21) 99999-9999',
            'data-mask': '(00) 00000-0000'
        })
    )
    
    discord_nick = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu_nick#1234'
        })
    )
    
    cep = forms.CharField(
        max_length=9,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '00000-000',
            'data-mask': '00000-000',
            'id': 'id_cep'
        })
    )
    
    endereco = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Rua, Avenida...',
            'id': 'id_endereco'
        })
    )
    
    numero = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número'
        })
    )
    
    complemento = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apto, Bloco... (opcional)'
        })
    )
    
    bairro = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Bairro',
            'id': 'id_bairro'
        })
    )
    
    cidade = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cidade',
            'id': 'id_cidade'
        })
    )
    
    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'password1', 'password2',
            'nome_completo', 'nome_social', 'cpf', 'telefone',
            'discord_nick', 'cep', 'endereco', 'numero',
            'complemento', 'bairro', 'cidade'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme a senha'
        })
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Remove formatação
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        
        # Valida CPF
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf_limpo):
            raise forms.ValidationError('CPF inválido.')
        
        # Verifica se já existe
        if Usuario.objects.filter(cpf=cpf_limpo).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        
        return cpf_limpo
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email


class UsuarioLoginForm(AuthenticationForm):
    """
    Formulário de login customizado
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha'
        })
    )


class UsuarioPerfilForm(forms.ModelForm):
    """
    Formulário de edição de perfil do usuário
    """
    
    class Meta:
        model = Usuario
        fields = [
            'nome_completo', 'nome_social', 'telefone',
            'discord_nick', 'cep', 'endereco', 'numero',
            'complemento', 'bairro', 'cidade'
        ]
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'data-mask': '(00) 00000-0000'
            }),
            'discord_nick': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'data-mask': '00000-000',
                'id': 'id_cep_edit'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_endereco_edit'
            }),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_bairro_edit'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_cidade_edit'
            }),
        }