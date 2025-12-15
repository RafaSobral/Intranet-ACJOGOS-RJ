from django import forms
from .models import Empresa
from validate_docbr import CNPJ


class EmpresaForm(forms.ModelForm):
    """
    Formulário para cadastro e edição de empresas
    """
    
    class Meta:
        model = Empresa
        fields = [
            'nome_fantasia', 'razao_social', 'cnpj', 'porte',
            'email', 'telefone', 'site',
            'cep', 'endereco', 'numero', 'complemento',
            'bairro', 'cidade', 'estado',
            'descricao', 'logo', 'data_fundacao',
            'publica'
        ]
        
        widgets = {
            'nome_fantasia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome Fantasia da Empresa'
            }),
            'razao_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Razão Social'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.000.000/0000-00',
                'data-mask': '00.000.000/0000-00'
            }),
            'porte': forms.Select(attrs={
                'class': 'form-select'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'contato@empresa.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(21) 99999-9999',
                'data-mask': '(00) 00000-0000'
            }),
            'site': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.empresa.com'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000',
                'data-mask': '00000-000',
                'id': 'id_cep_empresa'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua, Avenida...',
                'id': 'id_endereco_empresa'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sala, Andar... (opcional)'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro',
                'id': 'id_bairro_empresa'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
                'id': 'id_cidade_empresa'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'RJ'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva a empresa, suas atividades e especialidades...'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'data_fundacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'publica': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
        labels = {
            'nome_fantasia': 'Nome Fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'porte': 'Porte da Empresa',
            'email': 'E-mail de Contato',
            'telefone': 'Telefone',
            'site': 'Website',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'descricao': 'Descrição da Empresa',
            'logo': 'Logo',
            'data_fundacao': 'Data de Fundação',
            'publica': 'Tornar empresa visível publicamente',
        }
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        # Remove formatação
        cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
        
        # Valida CNPJ
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(cnpj_limpo):
            raise forms.ValidationError('CNPJ inválido.')
        
        # Verifica se já existe (exceto se estiver editando)
        if self.instance.pk:
            # Está editando
            if Empresa.objects.filter(cnpj=cnpj_limpo).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este CNPJ já está cadastrado.')
        else:
            # Está criando novo
            if Empresa.objects.filter(cnpj=cnpj_limpo).exists():
                raise forms.ValidationError('Este CNPJ já está cadastrado.')
        
        return cnpj_limpo
    
    def clean_site(self):
        site = self.cleaned_data.get('site')
        if site and not site.startswith(('http://', 'https://')):
            return f'https://{site}'
        return site


class EmpresaFiltroForm(forms.Form):
    """
    Formulário de filtros para listagem de empresas
    """
    busca = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nome...'
        })
    )
    
    cidade = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cidade'
        })
    )
    
    porte = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os portes')] + list(Empresa.PORTE_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )