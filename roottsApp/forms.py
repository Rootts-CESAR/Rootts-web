from django import forms

from .models import Encosta


class EncostaForm(forms.ModelForm):
    class Meta:
        model = Encosta
        fields = ('nome', 'descricao', 'local')
        