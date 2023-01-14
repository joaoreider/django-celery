from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Pessoa
from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw
from hashlib import sha256
from .tasks import cria_convite

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome = nome, email = email)
    pessoa.save()

    cria_convite.delay(nome, email)

    return render(request, 'cadastro_confirmado.html')

    
    