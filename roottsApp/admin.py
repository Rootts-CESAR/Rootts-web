from django.contrib import admin

from .models import Encosta


@admin.register(Encosta)
class EncostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local')
