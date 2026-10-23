from django.contrib import admin
from .models import Edicion, Categoria, Votacion, Opcion

admin.site.register(Edicion)
admin.site.register(Categoria)
admin.site.register(Votacion)

@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'votacion', 'votos')