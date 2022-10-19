from django.contrib import admin

from .models import *


@admin.register(Encosta)
class EncostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local')

@admin.register(Formulario_denuncia)
class FormAdmin(admin.ModelAdmin):
    list_display =('nome','data','titulo')


admin.site.register(User)

admin.site.register(EngineerUser)

admin.site.register(RegularUser)
