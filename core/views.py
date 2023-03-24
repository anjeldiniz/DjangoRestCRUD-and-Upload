from django.shortcuts import render, redirect
from django.conf import settings
from PIL import Image
from datetime import date
import os
from .models import Pessoa, MyFile


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})


def upload(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")

        mf = MyFile(title="minha_imagem", arq=file)
        mf.save()
        """
        img = Image.open(file)
        path = os.path.join(settings.BASE_DIR, f'media/{file.name}-{date.today()}.png')
        img = img.save(path)
        print(file)
        """
        return render(request, "index.html")


def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.tml', {'pessoas': pessoas})


def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})


def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
