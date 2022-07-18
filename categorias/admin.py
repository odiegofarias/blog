from django.contrib import admin
from . models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categ')
    list_display_links = ('id', 'nome_categ')


admin.site.register(Categoria, CategoriaAdmin)
