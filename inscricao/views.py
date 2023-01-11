from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Pessoa
from django.core.mail import send_mail

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome = nome, email = email)
    pessoa.save()
    send_mail('TESTE ENVIANDO EMAIL DJANGO', 'Lorem ipsum ..', 'joaopauloj1408@gmail.com', recipient_list=[email, ])
    return HttpResponse('Sucesso')

    
    