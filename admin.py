from django.contrib import admin
from .models import Receita, Despesa, Balanco, Titulo

class DespesaInline(admin.TabularInline):
    model = Despesa
    extra = 2

class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 2


class ConfigAdmin(admin.ModelAdmin):
    inlines = [DespesaInline]
    inlines1 = [ReceitaInline]
    list_filter = ['data_pub', 'data_fim']
    search_fields = ['text']

admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Balanco)
admin.site.register(Titulo)