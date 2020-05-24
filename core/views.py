from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import Grupo, Formulario, Inscrito, Newsletter

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
import threading
from django.utils import translation

from django.utils.translation import gettext as _

def email(assunto, mensagem, remetente, destinatarios, template):
    send_mail(assunto, mensagem, remetente, destinatarios, html_message=template)

def enviar_email(assunto = 'Teste', mensagem = 'Apenas mais um teste.', remetente = settings.EMAIL_HOST_USER, destinatarios = ['gabriel.costa.campos.13@gmail.com'], conteudo_template = ''):
    template = render_to_string('email/header.html', {}) + conteudo_template + render_to_string('email/footer.html', {})

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
            return redirect('/administracao')
        else:
            messages.warning(request, _('loginInvalido'))
            contexto = {'email': email, 'mensagem': _('loginInvalido')}
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
    grupo = Grupo.objects.get(responsavel=request.user)
    
    contexto = {'grupo': grupo}

    return render(request, 'administracao/newsletter.html', contexto) 

@login_required(login_url='/login')
def criar_newsletter(request):
    grupo = Grupo.objects.get(responsavel=request.user)
    setattr(grupo, 'informacao', grupo.informacoes.first)
    
    contexto = {'grupo': grupo}

    return render(request, 'administracao/criar_newsletter.html', contexto) 

@login_required(login_url='/login')
def enviar_newsletter(request):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        assunto = request.POST.get('assunto', '')
        mensagem = request.POST.get('mensagem', '')

        newsletter = Newsletter.objects.create(assunto=assunto, mensagem=mensagem)

        grupo.newsletters.add(newsletter)

        assunto = 'Novidades de {} - UFPI'.format(grupo.sigla.upper())
        mensagem_email = 'Assunto da newsletter de {}: {}\nPara visualizar a newsletter completa tente ativar a visualização de HTML.'.format(grupo.sigla.upper(), newsletter.assunto)
        destinatarios = Inscrito.objects.values_list('email', flat=True)

        conteudo_email = '<h2>Assunto da newsletter de {}: {}</h2>'.format(grupo.sigla.upper(), newsletter.assunto)
        conteudo_email += newsletter.mensagem

        enviar_email(assunto=assunto, mensagem=mensagem_email, destinatarios=destinatarios, conteudo_template=conteudo_email)       

        messages.success(request, 'Newsletter enviada com sucesso.')
    except:
        messages.warning(request, 'Não foi possível enviar a newsletter. Por favor, tente novamente.')

    return redirect('/newsletter') 

def grupo(request, sigla, idioma = None):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    categorias = []
    subcategorias = []

    for publicacao in grupo.publicacoes.all():
        if publicacao.categoria not in categorias:
            categorias.append(publicacao.categoria)
        if publicacao.subcategoria not in subcategorias:
            subcategorias.append(publicacao.subcategoria)

    if idioma:
        for informacao in grupo.informacoes.all():
            if idioma == informacao.idioma.sigla:
                setattr(grupo, 'informacao', informacao)
                translation.activate(idioma)
    else:
        setattr(grupo, 'informacao', grupo.informacoes.first)
        translation.activate(grupo.informacoes.first().idioma.sigla)

    setattr(grupo, 'categorias', categorias)
    setattr(grupo, 'subcategorias', subcategorias)

    contexto = {'grupo': grupo}

    return render(request, 'template/grupo.html', contexto)

def url_redirecionamento(sigla, idioma):
    url = '/' + str(sigla)

    if idioma:
        url += '/' + str(idioma)

    return url
    
def formulario(request, sigla, idioma = None):
    try: 
        grupo = get_object_or_404(Grupo, sigla=sigla)

        formulario = Formulario.objects.create(
            nome = request.POST.get('nome', ''),
            email = request.POST.get('email', ''),
            assunto = request.POST.get('assunto', ''),
            mensagem = request.POST.get('mensagem', '')
        )

        grupo.formularios.add(formulario)

        assunto = 'Novo contato em {}'.format(grupo.sigla.upper())
        mensagem = 'Alguém está tentando entrar em contato pelo formulário de contato na página do {}. Abaixo estão as informações enviadas:\nRemetente: {} - {}\nAssunto: {}\nMensagem: {}'.format(grupo.sigla.upper(), formulario.nome, formulario.email, formulario.assunto, formulario.mensagem)
        destinatarios = [grupo.responsavel.email, formulario.email]

        conteudo_email = '<h2>Alguém está tentando entrar em contato pelo formulário de contato na página do {}. Abaixo estão as informações enviadas:</h2>'.format(grupo.sigla.upper())
        conteudo_email += '<div class="card">'
        conteudo_email += '    <h3>Remetente: {} - {}</h3>'.format(formulario.nome, formulario.email)
        conteudo_email += '    <h4>Assunto: {}</h4>'.format(formulario.assunto)
        conteudo_email += '    <p>Mensagem: {}</p>'.format(formulario.mensagem)
        conteudo_email += '</div>'

        enviar_email(assunto=assunto, mensagem=mensagem, destinatarios=destinatarios, conteudo_template=conteudo_email)       

        messages.success(request, _('formularioEnviado'))
    except:
        messages.warning(request, _('formularioNaoEnviado'))

    url = url_redirecionamento(sigla, idioma)
    print(url)
    return redirect(url)

def inscrever(request, sigla, idioma = None):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    email = request.POST.get('email', '')
    inscrito = Inscrito.objects.create(email=email)

    grupo.inscritos.add(inscrito)

    messages.success(request, _('inscricaoNewssletterEnviada'))

    url = url_redirecionamento(sigla, idioma)
    return redirect(url)
