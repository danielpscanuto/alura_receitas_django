from django.contrib import admin
from pessoas.models import Pessoa
# Register your models here.

class ListaPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome','email')
    list_display_links = ('id', 'nome','email')
    search_fields = ('nome',)
    # list_filter = (' ',)
    list_per_page = 15

admin.site.register(Pessoa, ListaPessoas)