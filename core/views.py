from django.shortcuts import render, get_object_or_404
from .models import Grupo

def inicio(request):
    grupos = Grupo.objects.all()
    contexto = {'grupos': grupos}

    return render(request, 'inicio.html', contexto) 

def grupo(request, grupo):
    grupo = get_object_or_404(Grupo, sigla=grupo)

    categorias = []
    subcategorias = []

    for publicacao in grupo.informacoes.first().publicacoes.all():
        if publicacao.categoria not in categorias:
            categorias.append(publicacao.categoria)
        if publicacao.subcategoria not in subcategorias:
            subcategorias.append(publicacao.subcategoria)

    print(categorias, subcategorias)

    setattr(grupo, 'informacao', grupo.informacoes.first)
    setattr(grupo, 'categorias', categorias)
    setattr(grupo, 'subcategorias', subcategorias)

    contexto = {'grupo': grupo}

    return render(request, 'template/grupo.html', contexto)
