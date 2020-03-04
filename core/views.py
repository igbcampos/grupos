from django.shortcuts import render, get_object_or_404
from .models import Grupo

def inicio(request, grupo):
    grupo = get_object_or_404(Grupo, sigla=grupo)

    setattr(grupo, 'informacao', grupo.informacoes.first)

    contexto = {'grupo': grupo}

    return render(request, 'inicio.html', contexto)
