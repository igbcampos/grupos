from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import Grupo, Inscrito

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
import threading

def email(assunto, mensagem, remetente, destinatarios, template):
    send_mail(assunto, mensagem, remetente, destinatarios, html_message=template)

def enviar_email(assunto = 'Teste', mensagem = 'Apenas mais um teste.', remetente = settings.EMAIL_HOST_USER, destinatarios = ['gabriel.costa.campos.13@gmail.com'], template = '<html></html>'):
    template = render_to_string('email/header.html', {})
    template += render_to_string('email/footer.html', {})

    thread = threading.Thread(target=email, args=(assunto, mensagem, remetente, destinatarios, template))
    thread.start()

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

@login_required(login_url='/login')
def newsletter(request):
    contexto = {}

    return render(request, 'administracao/newsletter.html', contexto) 

@login_required(login_url='/login')
def criar_newsletter(request):
    grupo = Grupo.objects.get(responsavel=request.user)
    setattr(grupo, 'informacao', grupo.informacoes.first)
    
    contexto = {'grupo': grupo}

    return render(request, 'administracao/criar_newsletter.html', contexto) 

def grupo(request, sigla):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    categorias = []
    subcategorias = []

    for publicacao in grupo.informacoes.first().publicacoes.all():
        if publicacao.categoria not in categorias:
            categorias.append(publicacao.categoria)
        if publicacao.subcategoria not in subcategorias:
            subcategorias.append(publicacao.subcategoria)

    setattr(grupo, 'informacao', grupo.informacoes.first)
    setattr(grupo, 'categorias', categorias)
    setattr(grupo, 'subcategorias', subcategorias)

    contexto = {'grupo': grupo}

    return render(request, 'template/grupo.html', contexto)

def inscrever(request, sigla):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    email = request.POST.get('email', '')
    inscrito = Inscrito.objects.create(email=email)

    grupo.inscritos.add(inscrito)

    messages.success(request, 'E-mail registrado com sucesso na nossa newsletter. Em breve daremos notícias.')
    return redirect('/' + str(sigla))
