from cProfile import label
from django import forms

from .models import Encosta
from .models import Formulario_denuncia

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
        Model = Encosta
        fields = ('nome', 'local')
        labels = {
            'nome': 'Nome',
            'local': 'Local',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['local'].widget.attrs.update({'class': 'form-control'})
  
class denunciaForm(forms.ModelForm):
    class Meta:
        model = Formulario_denuncia
        fields = "__all__"
        widgets = {
            'data': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'})

        }
      
    
