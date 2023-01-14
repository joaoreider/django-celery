from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw
from hashlib import sha256

@shared_task
def cria_convite(nome, email):
    template = os.path.join(settings.STATIC_ROOT, 'img/convite.png')
    img = Image.open(template)
    img_escrever = ImageDraw.Draw(img)
    img_escrever.text((50,50), nome, fill=(200, 89, 255))
    key = "sdfjkhsdkfjhsfjsdhf$$##@@DFSDFSFFFFDSSSfdfdfjsdof"
    token = sha256((email + key).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)
    send_mail('TESTE ENVIANDO EMAIL DJANGO', f'SEU CONVITE: \n https:127.0.0.1:8000/media/convites/{token}.png', 'joaopauloj1408@gmail.com', recipient_list=[email, ])

