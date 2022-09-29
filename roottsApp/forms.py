from cProfile import label
from django import forms

from .models import Encosta

# only for create
class EncostaForm(forms.ModelForm):
    class Meta:
        model = Encosta
        fields = ('nome', 'descricao', 'local')
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'local': 'Local',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['local'].widget.attrs.update({'class': 'form-control'})

# only for update
class EncostaFormUpdate(forms.ModelForm):
    class Meta:
        model = Encosta
        fields = ('nome', 'local')
        labels = {
            'nome': 'Nome',
            'local': 'Local',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['local'].widget.attrs.update({'class': 'form-control'})
  
