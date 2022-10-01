from django import forms

from .models import Encosta
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
            'data': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
            'descricao': forms.Textarea(attrs={'class': 'descricao','placeholder':'Faça uma breve descrição do que está acontecendo.'}),
            'nome': forms.TextInput(attrs={'class': 'nome','placeholder':'Digite seu nome'}),
            'titulo': forms.TextInput(attrs={'class': 'titulo','placeholder':'Informe o Assunto'})
        }

      
    
