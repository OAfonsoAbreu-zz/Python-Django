from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.
def evento(request, nome_evento):
    novo_evento = Evento.objects.get(titulo=nome_evento)
    return HttpResponse('<h1>O evento se chama {} e será em {} </h1>'.format(novo_evento.titulo, novo_evento.data_evento.strftime('%d/%m/%Y às %Hh%M')))
