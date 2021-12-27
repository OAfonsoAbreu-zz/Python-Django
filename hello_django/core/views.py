from django.shortcuts import render, HttpResponse
from .model.calculadora import Calculadora

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome,idade))

def somar(request, a, b):
    calculadora = Calculadora()
    return HttpResponse('<h1>Soma:</h1><br><h2>Resultado de {a} + {b} = {resultado}</h2>'.format(a=a, b=b, resultado=calculadora.somar(a,b)))

def subtrair(request, a, b):
    calculadora = Calculadora()
    return HttpResponse('<h1>Subtração:</h1><br><h2>Resultado de {a} - {b} = {resultado}</h2>'.format(a=a, b=b, resultado=calculadora.subtrair(a,b)))

def multiplicar(request, a, b):
    calculadora = Calculadora()
    return HttpResponse('<h1>Multiplicação:</h1><br><h2>Resultado de {a} x {b} = {resultado}</h2>'.format(a=a, b=b, resultado=calculadora.multiplicar(a,b)))

def dividir(request, a, b):
    calculadora = Calculadora()
    return HttpResponse('<h1>Divisão:</h1><br><h2>Resultado de {a} / {b} = {resultado}</h2>'.format(a=a, b=b, resultado=calculadora.dividir(a,b)))
