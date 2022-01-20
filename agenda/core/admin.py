from django.contrib import admin
from core.models import Evento

#Personalizar a vizualização da tabela no portal Admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao') #Ordem e colunas da classe que irão aparecer no portal Admin
    list_filter = ('usuario','data_evento',) #Criar filtro no Admin (tem que ter virgula no final para não dar erro)

# Register your models here.
#Para registrar 'Evento' no portal Admin
admin.site.register(Evento, EventoAdmin) #Associando Evento a EventoAdmin