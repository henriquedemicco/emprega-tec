from django.contrib import admin
from core.models import Vaga, Candidatura

# Register your models here.

class VagaAdmin(admin.ModelAdmin):
    list_display = ('nome_vaga',)

admin.site.register(Vaga, VagaAdmin)

admin.site.register(Candidatura)
