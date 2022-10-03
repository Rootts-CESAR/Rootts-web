from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Encosta, Regular_user, User, Regular_user, Engineer
from .models import Formulario_denuncia

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
        )
        labels = {
            'declividade': 'Declividade',
            'numeroConstrucoes': 'Numero de Construções por m²',
            'numeroCasas': 'Numero de Casas',
            'coeficienteUmidade': 'Coeficiente de Umidade',
            'proximidadeRedeViarias': 'Proximidade de Redes Viarias por m²',
            'proximidadeCorposLiquidos': 'Proximidade de Corpos Liquidos por m²',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['declividade'].widget.attrs.update({'class': 'form-control'})
        self.fields['numeroConstrucoes'].widget.attrs.update({'class': 'form-control'})
        self.fields['coeficienteUmidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeRedeViarias'].widget.attrs.update({'class': 'form-control'})
        self.fields['proximidadeCorposLiquidos'].widget.attrs.update({'class': 'form-control'})


class denunciaForm(forms.ModelForm):
    class Meta:
        model = Formulario_denuncia
        fields = "__all__"
        widgets = {
            'data': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'min': '1970-01-01', 'max': '2050-12-31', 'class': 'form-control', 'required': True}),
            'descricao': forms.Textarea(attrs={'class': 'descricao','placeholder':'Faça uma breve descrição do que está acontecendo.', 'required': True, 'minlength': '10', 'maxlength': '500'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'return event.charCode >= 65 && event.charCode <= 122 || event.charCode == 32', 'placeholder': 'Digite seu nome', 'required': True}),
            'titulo': forms.TextInput(attrs={'class': 'titulo','placeholder':'Informe o Assunto', 'required': True, 'minlength': '10', 'maxlength': '120'}),
        }

      
class Regular_user_registration_form(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    cep = forms.IntegerField(required=True)
    street = forms.CharField(required=True)
    number = forms.IntegerField(required=True)
    neighborhood = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save_data(self):
        user = super().save(commit=False)
        regular_user.first_name = self.cleaned_data.get("first_name")
        regular_user.last_name = self.cleaned_data.get("last_name")
        regular_user.phone_number = self.cleaned_data.get("phone_number")
        user.save()
        regular_user = Regular_user.objects.create(user=user)
        regular_user.cep = self.cleaned_data.get("cep")
        regular_user.street = self.cleaned_data.get("street")
        regular_user.number = self.cleaned_data.get("number")
        regular_user.neighborhood = self.cleaned_data.get("neighborhood")
        regular_user.save()
        return Regular_user
        
class Engineer_registration_form(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    crea = forms.IntegerField(required=True) 

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save_data(self):
        user = super().save(commit=False)
        Engineer.first_name = self.cleaned_data.get("first_name")
        Engineer.last_name = self.cleaned_data.get("last_name")
        Engineer.phone_number = self.cleaned_data.get("phone_number")
        user.save()
        Engineer = Engineer.objects.create(user=user)
        Engineer.crea = self.cleaned_data.get("crea")
        Engineer.save()
        return Engineer
