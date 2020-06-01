from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import Documento, Idioma, Inscrito, Pesquisador, Instituicao, Linha, Servico, Publicacao, Premiacao, Portifolio, Projeto, Formulario, Informacao, Newsletter, Grupo

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
    idiomas = Idioma.objects.values_list('nome', flat=True)
    idiomas_ativos = []

    for informacao in grupo.informacoes.all():
        idiomas_ativos.append(informacao.idioma.nome)

    setattr(grupo, 'informacao', grupo.informacoes.first)
    
    contexto = {'grupo': grupo, 'idiomas': idiomas, 'idiomas_ativos': idiomas_ativos}

    return render(request, 'administracao/administracao.html', contexto)

def copiar_pesquisadores(informacao_portugues, informacao_destino):
    for pesquisador in informacao_portugues.pesquisadores.all():
        pesquisador.pk = None
        pesquisador.save()

        informacao_destino.pesquisadores.add(pesquisador)
        informacao_destino.save()

def copiar_instituicoes(informacao_portugues, informacao_destino):
    for instituicao in informacao_portugues.instituicoes.all():
        instituicao.pk = None
        instituicao.save()

        informacao_destino.instituicoes.add(instituicao)
        informacao_destino.save()

def copiar_linhas(informacao_portugues, informacao_destino):
    for linha in informacao_portugues.linhas.all():
        linha.pk = None
        linha.save()

        informacao_destino.linhas.add(linha)
        informacao_destino.save()

def copiar_servicos(informacao_portugues, informacao_destino):
    for servico in informacao_portugues.servicos.all():
        servico.pk = None
        servico.save()

        informacao_destino.servicos.add(servico)
        informacao_destino.save()

def copiar_publicacoes(informacao_portugues, informacao_destino):
    for publicacao in informacao_portugues.publicacoes.all():
        publicacao.pk = None
        publicacao.save()

        informacao_destino.publicacoes.add(publicacao)
        informacao_destino.save()

def copiar_premiacoes(informacao_portugues, informacao_destino):
    for premiacao in informacao_portugues.premiacoes.all():
        premiacao.pk = None
        premiacao.save()

        informacao_destino.premiacoes.add(premiacao)
        informacao_destino.save()

def copiar_portifolios(informacao_portugues, informacao_destino):
    for portifolio in informacao_portugues.portifolio.all():
        portifolio.pk = None
        portifolio.save()

        informacao_destino.portifolio.add(portifolio)
        informacao_destino.save()

def copiar_projetos(informacao_portugues, informacao_destino):
    for projeto in informacao_portugues.projetos.all():
        projeto.pk = None
        projeto.save()

        informacao_destino.projetos.add(projeto)
        informacao_destino.save()

@login_required(login_url='/login')
def salvar_sobre(request):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        idiomas = []

        grupo.nome = request.POST.get('nome', '')
        grupo.sigla = request.POST.get('sigla', '')
        #grupo.mapa = request.POST.get('mapa', '')
        grupo.telefone = request.POST.get('telefone', '')
        grupo.email = request.POST.get('email', '')
        grupo.endereco = request.POST.get('endereco', '')
        grupo.facebook = request.POST.get('facebook', '')
        grupo.twitter = request.POST.get('twitter', '')
        grupo.instagram = request.POST.get('instagram', '')

        for informacao in grupo.informacoes.all():
            idiomas.append(informacao.idioma.nome)

        for informacao in grupo.informacoes.all():
            grupo.descricao = request.POST.get('descricao-' + informacao.idioma.sigla, '')
            grupo.descricao_infraestrutura = request.POST.get('descricao-infraestrutura-' + informacao.idioma.sigla, '')

        for informacao in grupo.informacoes.all():
            if informacao.idioma.nome not in request.POST.getlist('idiomas', ''):
                informacao.delete()

        for idioma in request.POST.getlist('idiomas', ''):
            if idioma not in idiomas:
                for informacao in grupo.informacoes.all():
                    if informacao.idioma.sigla == 'pt':
                        informacao_portugues = Informacao.objects.get(pk = informacao.pk)

                        nova_informacao = informacao
                        nova_informacao.pk = None
                        nova_informacao.idioma = Idioma.objects.get(nome = idioma)
                        nova_informacao.save()

                        grupo.informacoes.add(nova_informacao)

                        copiar_pesquisadores(informacao_portugues, nova_informacao)
                        copiar_instituicoes(informacao_portugues, nova_informacao)
                        copiar_linhas(informacao_portugues, nova_informacao)
                        copiar_servicos(informacao_portugues, nova_informacao)
                        copiar_publicacoes(informacao_portugues, nova_informacao)
                        copiar_premiacoes(informacao_portugues, nova_informacao)
                        copiar_portifolios(informacao_portugues, nova_informacao)
                        copiar_projetos(informacao_portugues, nova_informacao)

        if 'imagem' in request.FILES:
            grupo.imagem = request.FILES['imagem']
        if 'imagem-infraestrutura1' in request.FILES:
            grupo.imagem_infraestrutura1 = request.FILES['imagem-infraestrutura1']
        if 'imagem-infraestrutura2' in request.FILES:
            grupo.imagem_infraestrutura2 = request.FILES['imagem-infraestrutura2']
        if 'imagem-infraestrutura3' in request.FILES:
            grupo.imagem_infraestrutura3 = request.FILES['imagem-infraestrutura3']

        grupo.save()
        
        messages.warning(request, 'As informação do grupo foram salvas com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do grupo. Por favor, tente novamente.')
    
    return redirect('/administracao') 

@login_required(login_url='/login')
def salvar_pesquisador(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    pesquisador = Pesquisador.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                        descricao_completa = request.POST.get('descricao-completa', ''),
                        lattes = request.POST.get('lattes', ''),
                        orcid = request.POST.get('orcid', '')
                    )

                    if 'imagem' in request.FILES:
                        pesquisador.imagem = request.FILES['imagem']
                        pesquisador.save()

                    informacao.pesquisadores.add(pesquisador)
                else:
                    pesquisador = Pesquisador.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                        descricao_completa = request.POST.get('descricao-completa', ''),
                        lattes = request.POST.get('lattes', ''),
                        orcid = request.POST.get('orcid', '')
                    )

                    if 'imagem' in request.FILES:
                        pesquisador.imagem = request.FILES['imagem']
                        pesquisador.save()

                    informacao.pesquisadores.add(pesquisador)

            messages.warning(request, 'Pesquisador cadastrado com sucesso.')
        else:
            pesquisador = Pesquisador.objects.get(pk=pk)

            pesquisador.nome = request.POST.get('nome', '')
            pesquisador.descricao = request.POST.get('descricao', '')
            pesquisador.descricao_completa = request.POST.get('descricao-completa', '')
            pesquisador.lattes = request.POST.get('lattes', '')
            pesquisador.orcid = request.POST.get('orcid', '')

            if 'imagem' in request.FILES:
                pesquisador.imagem = request.FILES['imagem']
                
            pesquisador.save()

            messages.warning(request, 'Pesquisador salvo com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do pesquisador. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_pesquisador(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao

        copiar_pesquisadores(informacao_portugues, informacao_destino)

        messages.warning(request, 'Pesquisadores copiados com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações dos pesquisadores. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_pesquisador(request, pk):
    try:
        Pesquisador.objects.get(pk=pk).delete()

        messages.warning(request, 'O pesquisador selecionado foi excluido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir o pesquisador selecionado.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_instituicao(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    instituicao = Instituicao.objects.create(
                        nome = request.POST.get('nome', ''),
                        categoria = request.POST.get('categoria', ''),
                    )

                    if 'imagem' in request.FILES:
                        instituicao.imagem = request.FILES['imagem']
                        instituicao.save()

                    informacao.instituicoes.add(instituicao)
                else:
                    instituicao = Instituicao.objects.create(
                        nome = request.POST.get('nome', ''),
                        categoria = request.POST.get('categoria', ''),
                    )

                    if 'imagem' in request.FILES:
                        instituicao.imagem = request.FILES['imagem']
                        instituicao.save()

                    informacao.instituicoes.add(instituicao)

            messages.warning(request, 'Parceiro cadastrado com sucesso.')
        else:
            instituicao = Instituicao.objects.get(pk=pk)

            instituicao.nome = request.POST.get('nome', '')
            instituicao.categoria = request.POST.get('categoria', '')

            if 'imagem' in request.FILES:
                instituicao.imagem = request.FILES['imagem']
                
            instituicao.save()

            messages.warning(request, 'Parceiro salvo com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do parceiro. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_instituicao(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao

        copiar_instituicoes(informacao_portugues, informacao_destino)

        messages.warning(request, 'Parceiros copiados com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações dos parceiros. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_instituicao(request, pk):
    try:
        Instituicao.objects.get(pk=pk).delete()

        messages.warning(request, 'O parceiro selecionado foi excluido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir o parceiro selecionada.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_linha(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    linha = Linha.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                    )

                    informacao.linhas.add(linha)
                else:
                    linha = Linha.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                    )

                    informacao.linhas.add(linha)

            messages.warning(request, 'Linha de pesquisa cadastrada com sucesso.')
        else:
            linha = Linha.objects.get(pk=pk)

            linha.nome = request.POST.get('nome', '')
            linha.descricao = request.POST.get('descricao', '')
                
            linha.save()

            messages.warning(request, 'Linha de pesquisa salva com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações da linha de pesquisa. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_linha(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao

        copiar_linhas(informacao_portugues, informacao_destino)

        messages.warning(request, 'Linhas de pesquisa copiadas com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações das linhas de pesquisa. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_linha(request, pk):
    try:
        Linha.objects.get(pk=pk).delete()

        messages.warning(request, 'A linha de pesquisa selecionado foi excluida com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir a linha de pesquisa selecionada.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_servico(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    servico = Servico.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                    )

                    informacao.servicos.add(servico)
                else:
                    servico = Servico.objects.create(
                        nome = request.POST.get('nome', ''),
                        descricao = request.POST.get('descricao', ''),
                    )

                    informacao.servicos.add(servico)

            messages.warning(request, 'Serviço cadastrado com sucesso.')
        else:
            servico = Servico.objects.get(pk=pk)

            servico.nome = request.POST.get('nome', '')
            servico.descricao = request.POST.get('descricao', '')
                
            servico.save()

            messages.warning(request, 'Serviço salvo com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do serviço. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_servico(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao

        copiar_servicos(informacao_portugues, informacao_destino)

        messages.warning(request, 'Serviços copiados com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações dos serviços. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_servico(request, pk):
    try:
        Servico.objects.get(pk=pk).delete()

        messages.warning(request, 'O serviço selecionado foi excluido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir o serviço selecionado.')
    
    return redirect('/administracao')

def categoria(subcategoria):
    if subcategoria == 'Artigos completos publicados em periódicos' or subcategoria == 'Artigos aceitos para publicação' or subcategoria == 'Livros e capítulos' or subcategoria == 'Texto em jornal ou revista (magazine)' or subcategoria == 'Trabalhos publicados em anais de eventos' or subcategoria == 'Apresentação de trabalho e palestra' or subcategoria == 'Partitura musical' or subcategoria == 'Tradução' or subcategoria == 'Prefácio, posfácio' or subcategoria == 'Outra produção bibliográfica':
        return 'Produção Bibliográfica'
    if subcategoria == 'Assessoria e consultoria' or subcategoria == 'Extensão tecnológica' or subcategoria == 'Programa de computador sem registro' or subcategoria == 'Produtos' or subcategoria == 'Processos ou técnicas' or subcategoria == 'Trabalhos técnicos' or subcategoria == 'Cartas, mapas ou similares' or subcategoria == 'Curso de curta duração ministrado' or subcategoria == 'Desenvolvimento de material didático ou instrucional' or subcategoria == 'Editoração' or subcategoria == 'Manutenção de obra artística' or subcategoria == 'Maquete' or subcategoria == 'Entrevistas, mesas redondas, programas e comentários na mídia' or subcategoria == 'Relatório de pesquisa' or subcategoria == 'Redes sociais, websites e blogs' or subcategoria == 'Outra produção técnica':
        return 'Produção Técnica'
    if subcategoria == 'Artes cênicas' or subcategoria == 'Música' or subcategoria == 'Artes visuais' or subcategoria == 'Outra produção artística/cultural':
        return 'Outra produção artística/cultural'

@login_required(login_url='/login')
def salvar_publicacao(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    publicacao = Publicacao.objects.create(
                        nome = request.POST.get('nome', ''),
                        ano = request.POST.get('ano', ''),
                        descricao = request.POST.get('descricao', ''),
                        categoria = categoria(request.POST.get('subcategoria', '')),
                        subcategoria = request.POST.get('subcategoria', '')
                    )

                    informacao.publicacoes.add(publicacao)
                else:
                    publicacao = Publicacao.objects.create(
                        nome = request.POST.get('nome', ''),
                        ano = request.POST.get('ano', ''),
                        descricao = request.POST.get('descricao', ''),
                        categoria = categoria(request.POST.get('subcategoria', '')),
                        subcategoria = request.POST.get('subcategoria', '')
                    )

                    informacao.publicacoes.add(publicacao)

            messages.warning(request, 'Publicação cadastrada com sucesso.')
        else:
            publicacao = Publicacao.objects.get(pk=pk)

            publicacao.nome = request.POST.get('nome', '')
            publicacao.ano = request.POST.get('ano', '')
            publicacao.descricao = request.POST.get('descricao', '')
            publicacao.categoria = categoria(request.POST.get('subcategoria', ''))
            publicacao.subcategoria = request.POST.get('subcategoria', '')
                
            publicacao.save()

            messages.warning(request, 'Publicação salva com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações da publicação. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_publicacao(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao
        
        copiar_publicacoes(informacao_portugues, informacao_destino)

        messages.warning(request, 'Publicações copiadas com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações das publicações. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_publicacao(request, pk):
    try:
        Publicacao.objects.get(pk=pk).delete()

        messages.warning(request, 'A publicação selecionada foi excluida com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir a publicação selecionada.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_premiacao(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    premiacao = Premiacao.objects.create(
                        nome = request.POST.get('nome', ''),
                        ano = request.POST.get('ano', ''),
                        descricao = request.POST.get('descricao', '')
                    )

                    informacao.premiacoes.add(premiacao)
                else:
                    premiacao = Premiacao.objects.create(
                        nome = request.POST.get('nome', ''),
                        ano = request.POST.get('ano', ''),
                        descricao = request.POST.get('descricao', ''),
                    )

                    informacao.premiacoes.add(premiacao)

            messages.warning(request, 'Premiação cadastrada com sucesso.')
        else:
            premiacao = Premiacao.objects.get(pk=pk)

            premiacao.nome = request.POST.get('nome', '')
            premiacao.ano = request.POST.get('ano', '')
            premiacao.descricao = request.POST.get('descricao', '')
                
            premiacao.save()

            messages.warning(request, 'Premiação salva com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações da premiação. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_premiacao(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao
        
        copiar_premiacoes(informacao_portugues, informacao_destino)

        messages.warning(request, 'Premiações copiadas com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações das premiações. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_premiacao(request, pk):
    try:
        Premiacao.objects.get(pk=pk).delete()

        messages.warning(request, 'A premiação selecionada foi excluida com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir a premiação selecionada.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_portifolio(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    portifolio = Portifolio.objects.create(
                        nome = request.POST.get('nome', ''),
                        tipo = request.POST.get('tipo', ''),
                        link = request.POST.get('link', ''),
                    )

                    if 'imagem' in request.FILES:
                        portifolio.imagem = request.FILES['imagem']
                        portifolio.save()

                    informacao.portifolio.add(portifolio)
                else:
                    portifolio = Portifolio.objects.create(
                        nome = request.POST.get('nome', ''),
                        tipo = request.POST.get('tipo', ''),
                        link = request.POST.get('link', ''),
                    )

                    if 'imagem' in request.FILES:
                        portifolio.imagem = request.FILES['imagem']
                        portifolio.save()

                    informacao.portifolio.add(portifolio)

            messages.warning(request, 'Portifólio cadastrado com sucesso.')
        else:
            portifolio = Portifolio.objects.get(pk=pk)

            portifolio.nome = request.POST.get('nome', '')
            portifolio.tipo = request.POST.get('tipo', '')
            portifolio.link = request.POST.get('link', '')

            if 'imagem' in request.FILES:
                portifolio.imagem = request.FILES['imagem']
                
            portifolio.save()

            messages.warning(request, 'Portifólio salvo com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do portifólio. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_portifolio(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao
        
        copiar_portifolios(informacao_portugues, informacao_destino)

        messages.warning(request, 'Portifólio copiado com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações do portifólio. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_portifolio(request, pk):
    try:
        Portifolio.objects.get(pk=pk).delete()

        messages.warning(request, 'O portifólio selecionado foi excluido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir o portifólio selecionado.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def salvar_projeto(request, idioma, pk = None):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        if pk is None:
            for informacao in grupo.informacoes.all():
                if idioma != 'pt':
                    projeto = Projeto.objects.create(
                        titulo = request.POST.get('titulo', ''),
                        descricao = request.POST.get('descricao', ''),
                        coordenador = Pesquisador.objects.get(pk = request.POST.get('coordenador', ''),),
                        data_inicio = request.POST.get('data-inicio', '')
                    )

                    if request.POST.get('data-fim', ''):
                        projeto.data_fim = request.POST.get('data-fim', '')

                    for integrante in request.POST.getlist('integrantes', ''):
                        projeto.integrantes.add(Pesquisador.objects.get(pk=int(integrante)))
                    
                    projeto.save()

                    informacao.projetos.add(projeto)
                else:
                    projeto = Projeto.objects.create(
                        titulo = request.POST.get('titulo', ''),
                        descricao = request.POST.get('descricao', ''),
                        coordenador = Pesquisador.objects.get(pk = request.POST.get('coordenador', ''),),
                        data_inicio = request.POST.get('data-inicio', '')
                    )

                    if request.POST.get('data-fim', ''):
                        projeto.data_fim = request.POST.get('data-fim', '')

                    for integrante in request.POST.getlist('integrantes', ''):
                        projeto.integrantes.add(Pesquisador.objects.get(pk=int(integrante)))
                    
                    projeto.save()

                    informacao.projetos.add(projeto)

            messages.warning(request, 'Projeto cadastrado com sucesso.')
        else:
            projeto = Projeto.objects.get(pk=pk)

            projeto.titulo = request.POST.get('titulo', '')
            projeto.descricao = request.POST.get('descricao', '')
            projeto.coordenador = Pesquisador.objects.get(pk = request.POST.get('coordenador', ''))
            projeto.data_inicio = request.POST.get('data-inicio', '')

            if request.POST.get('data-fim', ''):
                projeto.data_fim = request.POST.get('data-fim', '')
            
            projeto.integrantes.clear()

            for integrante in request.POST.getlist('integrantes', ''):
                projeto.integrantes.add(Pesquisador.objects.get(pk=int(integrante)))
                
            projeto.save()

            messages.warning(request, 'Projeto salvo com sucesso.')
    except:
        messages.warning(request, 'Não foi possível salvar as informações do projeto. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def copiar_projeto(request, idioma):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        
        informacao_portugues = {}
        informacao_destino = {}

        for informacao in grupo.informacoes.all():
            if informacao.idioma.sigla == 'pt':
                informacao_portugues = informacao
            elif informacao.idioma.sigla == idioma:
                informacao_destino = informacao
        copiar_projetos(informacao_portugues, informacao_destino)

        messages.warning(request, 'Projetos copiados com sucesso.')
    except:
        messages.warning(request, 'Não foi possível copiar as informações dos projetos. Por favor, tente novamente.')
    
    return redirect('/administracao')

@login_required(login_url='/login')
def excluir_projeto(request, pk):
    try:
        Projeto.objects.get(pk=pk).delete()

        messages.warning(request, 'O projeto selecionado foi excluido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível excluir o projeto selecionado.')
    
    return redirect('/administracao')

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
        publicar = False

        if 'publicar' in request.POST:
            publicar = True

        newsletter = Newsletter.objects.create(assunto=assunto, mensagem=mensagem, publicado=publicar)

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

@login_required(login_url='/login')
def publicar_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    newsletter.publicado = True
    newsletter.save()

    messages.success(request, 'Newsletter publicada com sucesso.')

    return redirect('/newsletter')

@login_required(login_url='/login')
def despublicar_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    newsletter.publicado = False
    newsletter.save()

    messages.success(request, 'Newsletter removida das notícias com sucesso.')

    return redirect('/newsletter')     

@login_required(login_url='/login')
def documentos(request):
    grupo = Grupo.objects.get(responsavel=request.user)

    contexto = {'grupo': grupo}

    return render(request, 'administracao/documentos.html', contexto)   

@login_required(login_url='/login')
def salvar_documento(request):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)

        documento = Documento.objects.create(
            nome = request.POST.get('nome', ''),
            link = request.FILES['arquivo']
        )

        grupo.documentos.add(documento)
        grupo.save()

        messages.success(request, 'Documento enviado com sucesso.')
    except:
        messages.warning(request, 'Não foi possível enviar o documento. Por favor, tente novamente.')

    return redirect('/documentos')   

@login_required(login_url='/login')
def excluir_documento(request, pk):
    try:
        documento = get_object_or_404(Documento, pk = pk)
        documento.delete()

        messages.success(request, 'Documento removido com sucesso.')
    except:
        messages.warning(request, 'Não foi possível remover o documento selecionado. Por favor, tente novamente.')

    return redirect('/documentos')    

@login_required(login_url='/login')
def contatos(request):
    grupo = Grupo.objects.get(responsavel=request.user)

    contexto = {'grupo': grupo}

    return render(request, 'administracao/contatos.html', contexto)   

@login_required(login_url='/login')
def responder_contato(request, pk):
    try:
        grupo = Grupo.objects.get(responsavel=request.user)
        formulario = get_object_or_404(Formulario, pk = pk)

        assunto = 'Resposta à mensagem deixada em {}'.format(grupo.sigla.upper())
        mensagem = '{} está respondendo sua mensagem.\nMensagem: {}'.format(grupo.sigla.upper(), request.POST.get('mensagem', ''))
        destinatarios = [grupo.responsavel.email, formulario.email]

        conteudo_email = '<h2>{} está respondendo sua mensagem.</h2>'.format(grupo.sigla.upper())
        conteudo_email += '<div class="card">'
        conteudo_email += '    <p>Mensagem: {}</p>'.format(request.POST.get('mensagem', ''))
        conteudo_email += '</div>'

        enviar_email(assunto=assunto, mensagem=mensagem, destinatarios=destinatarios, conteudo_template=conteudo_email) 

        messages.success(request, 'Sua resposta foi enviada.')
    except:
        messages.warning(request, 'Não foi possível enviar sua resposta. Por favor, tente novamente.')

    return redirect('/contatos') 

def grupo(request, sigla, idioma = None):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    categorias = []
    subcategorias = []

    if idioma:
        for informacao in grupo.informacoes.all():
            if idioma == informacao.idioma.sigla:
                for publicacao in informacao.publicacoes.all():
                    if publicacao.categoria not in categorias:
                        categorias.append(publicacao.categoria)
                    if publicacao.subcategoria not in subcategorias:
                        subcategorias.append(publicacao.subcategoria)

                setattr(grupo, 'informacao', informacao)
                translation.activate(idioma)
    else:
        for publicacao in grupo.informacoes.first().publicacoes.all():
            if publicacao.categoria not in categorias:
                categorias.append(publicacao.categoria)
            if publicacao.subcategoria not in subcategorias:
                subcategorias.append(publicacao.subcategoria)

        setattr(grupo, 'informacao', grupo.informacoes.first)
        translation.activate(grupo.informacoes.first().idioma.sigla)

    setattr(grupo, 'categorias', categorias)
    setattr(grupo, 'subcategorias', subcategorias)

    contexto = {'grupo': grupo}

    return render(request, 'template/grupo.html', contexto)

def noticias(request, sigla, idioma = None):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    if idioma:
        for informacao in grupo.informacoes.all():
            if idioma == informacao.idioma.sigla:
                setattr(grupo, 'informacao', informacao)
                translation.activate(idioma)
    else:
        setattr(grupo, 'informacao', grupo.informacoes.first)
        translation.activate(grupo.informacoes.first().idioma.sigla)

    noticias = []

    for newsletter in grupo.newsletters.all():
        if newsletter.publicado:
            noticias.append(newsletter)

    setattr(grupo, 'noticias', noticias)
    translation.activate(idioma)

    contexto = {'grupo': grupo}

    return render(request, 'template/noticias.html', contexto)

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
    return redirect(url)

def inscrever(request, sigla, idioma = None):
    grupo = get_object_or_404(Grupo, sigla=sigla)

    email = request.POST.get('email', '')
    inscrito = Inscrito.objects.create(email=email)

    grupo.inscritos.add(inscrito)

    messages.success(request, _('inscricaoNewssletterEnviada'))

    url = url_redirecionamento(sigla, idioma)
    return redirect(url)
