from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import Grupo

def inicio(request):
    grupos = Grupo.objects.all()
    contexto = {'grupos': grupos}

    return render(request, 'inicio.html', contexto) 

def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'administracao/login.html', {})

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if '@' in email:
            email = User.objects.get(email=email).username

        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('/ciaten')
        else:
            messages.warning(request, 'Usuário e/ou senha incorretos. Por favor, tente novamente.')
            contexto = {'email': email, 'mensagem': 'Usuário e/ou senha incorretos. Por favor, tente novamente.'}
    else:
        raise Http404('Método de requisição não aceito')

@login_required(login_url='/login')
def deslogar(request):
    logout(request)
    
    return redirect('/')

@login_required(login_url='/login')
def administracao(request):
    grupo = Grupo.objects.get(responsavel=request.user)
    setattr(grupo, 'informacao', grupo.informacoes.first)
    
    contexto = {'grupo': grupo}

    return render(request, 'administracao/administracao.html', contexto) 

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
