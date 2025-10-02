from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'idade', 'ativo', 'telefone', 'data_cadastro', 'endereco', 'sexo', 'data_nascimento']
    list_filter = ['ativo', 'sexo']
    search_fields = ['nome', 'email']