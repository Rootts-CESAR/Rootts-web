from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import *

# only for create
class EncostaForm(forms.ModelForm):
    class Meta:
        model = Encosta
        fields = (
            'nome',
            'local',
            'latitude',
            'longitude',
            'declividade',
            'numeroConstrucoes',
            'coeficienteUmidade',
            'proximidadeRedeViarias',
            'proximidadeCorposLiquidos',
            'prioridadeEncosta',
        )
        labels = {
            'nome': 'Nome',
            'local': 'Local',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'declividade': 'Declividade',
            'numeroConstrucoes': 'Numero de Construções por m²',
            'numeroCasas': 'Numero de Casas',
            'coeficienteUmidade': 'Coeficiente de Umidade',
            'proximidadeRedeViarias': 'Proximidade de Redes Viarias por m²',
            'proximidadeCorposLiquidos': 'Proximidade de Corpos Liquidos por m²',
            'prioridadeEncosta': 'Nível de Risco de Deslizamento',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['local'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['declividade'].widget.attrs.update({'class': 'form-control'})
        self.fields['numeroConstrucoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['coeficienteUmidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeRedeViarias'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeCorposLiquidos'].widget.attrs.update({'class': 'form-control'})
        self.fields['prioridadeEncosta'].widget.attrs.update({'class': 'form-control'})

# only for update
class EncostaFormUpdate(forms.ModelForm):
    class Meta:
        model = Encosta
        fields = (
            'declividade',
            'numeroConstrucoes',
            'coeficienteUmidade',
            'proximidadeRedeViarias',
            'proximidadeCorposLiquidos',
            'prioridadeEncosta',
        )
        labels = {
            'declividade': 'Declividade',
            'numeroConstrucoes': 'Numero de Construções por m²',
            'numeroCasas': 'Numero de Casas',
            'coeficienteUmidade': 'Coeficiente de Umidade',
            'proximidadeRedeViarias': 'Proximidade de Redes Viarias por m²',
            'proximidadeCorposLiquidos': 'Proximidade de Corpos Liquidos por m²',
            'prioridadeEncosta': 'Nível de Risco de Deslizamento',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['declividade'].widget.attrs.update({'class': 'form-control'})
        self.fields['numeroConstrucoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['coeficienteUmidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeRedeViarias'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeCorposLiquidos'].widget.attrs.update({'class': 'form-control'})
        self.fields['prioridadeEncosta'].widget.attrs.update({'class': 'form-control'})


class denunciaForm(forms.ModelForm):
    class Meta:
        model = Formulario_denuncia
        fields = "__all__"
        widgets = {
            'endereco': forms.TextInput(attrs={'class': 'titulo','placeholder':'Informe o seu Endereço', 'required': True, 'minlength': '10', 'maxlength': '120'}),
            'data': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'min': '1970-01-01', 'max': '2050-12-31', 'class': 'form-control', 'required': True}),
            'descricao': forms.Textarea(attrs={'class': 'descricao','placeholder':'Faça uma breve descrição do que está acontecendo.', 'required': True, 'minlength': '10', 'maxlength': '500'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'return event.charCode >= 65 && event.charCode <= 122 || event.charCode == 32', 'placeholder': 'Digite seu nome', 'required': True}),
            'titulo': forms.TextInput(attrs={'class': 'titulo','placeholder':'Informe o Assunto', 'required': True, 'minlength': '10', 'maxlength': '120'}),
            'aprovado':forms.CheckboxInput(attrs={'class':'aprovado','id': 'myonoffswitch'})
            }
        labels = {
            'aprovado' : '',
            'descricao':'Descrição'
            }


      
class RegularUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Senhas não conferem")
        return password2
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        user.save()
        regular = RegularUser.objects.create(user=user)
        return user
    

class EngineerUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    crea = forms.CharField(label='CREA', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'crea', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Senhas não conferem")
        return password2
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        user.is_engineer = True
        user.save()
        engineer = EngineerUser.objects.create(user=user)
        engineer.crea = self.cleaned_data.get('crea')
        engineer.save()
        return user