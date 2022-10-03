from django.contrib import admin

from .models import Encosta,Formulario_denuncia


@admin.register(Encosta)
class EncostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local')

@admin.register(Formulario_denuncia)
class FormAdmin(admin.ModelAdmin):
    list_display =('nome','data','titulo')
