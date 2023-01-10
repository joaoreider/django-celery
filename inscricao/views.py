from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Pessoa

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')

    try:
        pessoa = Pessoa(nome = nome, email = email)
        pessoa.save()

        return HttpResponse('Sucesso')
    
    except:

        return HttpResponse('Erro interno do sistema')