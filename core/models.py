from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import os
from uuid import uuid4

def caminho(instance, filename):
    nome_caminho = 'imagens/'
    ext = filename.split('.')[-1]
    
    if instance.pk:
        nome_arquivo = '{}.{}'.format(instance.pk, ext)
    else:
        nome_arquivo = '{}.{}'.format(uuid4().hex, ext)

    return os.path.join(nome_caminho, nome_arquivo)

class Idioma(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.ImageField(upload_to=caminho)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class Pesquisador(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.ImageField(upload_to=caminho)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    descricao_completa = models.TextField(max_length=300, blank=True, null=True)
    lattes = models.CharField(max_length=256, blank=True, null=True)
    orcid = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Pesquisador'
        verbose_name_plural = 'Pesquisadores'

class Instituicao(models.Model):
    categorias = [('Nacional', 'Nacional'), ('Internacional', 'Internacional')]

    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.ImageField(upload_to=caminho)
    categoria = models.CharField(max_length=256, blank=True, null=True, choices=categorias)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Parceiros/Colaboradores'
        verbose_name_plural = 'Parceiros/Colaboradores'

class Linha(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Linha de Pesquisa'
        verbose_name_plural = 'Linhas de Pesquisa'

class Servico(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Publicacao(models.Model):
    categorias = [
        ('Produção Bibliográfica', 'Produção Bibliográfica'),
        ('Produção Técnica', 'Produção Técnica'),
        ('Outra produção artística/cultural', 'Outra produção artística/cultural')
    ]

    subcategorias = [
        ('Artigos completos publicados em periódicos', 'Artigos completos publicados em periódicos'),
        ('Artigos aceitos para publicação', 'Artigos aceitos para publicação'),
        ('Livros e capítulos', 'Livros e capítulos'),
        ('Texto em jornal ou revista (magazine)', 'Texto em jornal ou revista (magazine)'),
        ('Trabalhos publicados em anais de eventos', 'Trabalhos publicados em anais de eventos'),
        ('Apresentação de trabalho e palestra', 'Apresentação de trabalho e palestra'),
        ('Partitura musical', 'Partitura musical'),
        ('Tradução', 'Tradução'),
        ('Prefácio, posfácio', 'Prefácio, posfácio'),
        ('Outra produção bibliográfica', 'Outra produção bibliográfica'),
        ('Assessoria e consultoria', 'Assessoria e consultoria'),
        ('Extensão tecnológica', 'Extensão tecnológica'),
        ('Programa de computador sem registro', 'Programa de computador sem registro'),
        ('Produtos', 'Produtos'),
        ('Processos ou técnicas', 'Processos ou técnicas'),
        ('Trabalhos técnicos', 'Trabalhos técnicos'),
        ('Cartas, mapas ou similares', 'Cartas, mapas ou similares'),
        ('Curso de curta duração ministrado', 'Curso de curta duração ministrado'),
        ('Desenvolvimento de material didático ou instrucional', 'Desenvolvimento de material didático ou instrucional'),
        ('Editoração', 'Editoração'),
        ('Manutenção de obra artística', 'Manutenção de obra artística'),
        ('Maquete', 'Maquete'),
        ('Entrevistas, mesas redondas, programas e comentários na mídia', 'Entrevistas, mesas redondas, programas e comentários na mídia'),
        ('Relatório de pesquisa', 'Relatório de pesquisa'),
        ('Redes sociais, websites e blogs', 'Redes sociais, websites e blogs'),
        ('Outra produção técnica', 'Outra produção técnica'),
        ('Artes cênicas', 'Artes cênicas'),
        ('Música', 'Música'),
        ('Artes visuais', 'Artes visuais'),
        ('Outra produção artística/cultural', 'Outra produção artística/cultural')
    ]

    nome = models.CharField(max_length=256, blank=True, null=True)
    ano = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    categoria = models.CharField(max_length=256, blank=True, null=True, choices=categorias)
    subcategoria = models.CharField(max_length=256, blank=True, null=True, choices=subcategorias)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Produção'
        verbose_name_plural = 'Produções'

class Premiacao(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    ano = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Premiação'
        verbose_name_plural = 'Premiações'

class Portifolio(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Portifolio'
        verbose_name_plural = 'Portifolios'

class Projeto(models.Model):
    titulo = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.TextField(max_length=1024, blank=True, null=True)
    coordenador = models.ForeignKey(Pesquisador, related_name='coordenador', null=True, blank=True, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(Pesquisador)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta():
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

class Informacao(models.Model):
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    descricao_infraestrutura = models.TextField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.descricao

    class Meta():
        verbose_name = 'Informação'
        verbose_name_plural = 'Informações'

class Formulario(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=256, blank=False, null=False)
    email = models.CharField(verbose_name='E-mail', max_length=256, blank=False, null=False)
    assunto = models.CharField(verbose_name='Assunto', max_length=256, blank=False, null=False)
    mensagem = models.TextField(verbose_name='Mensagem', blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Formulário'
        verbose_name_plural = 'Formulários'

class Inscrito(models.Model):
    email = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'

class Newsletter(models.Model):
    assunto = models.CharField(verbose_name='Assunto', max_length=256, blank=False, null=False)
    mensagem = models.TextField(verbose_name='Mensagem', blank=False, null=False)
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)

    def __str__(self):
        return self.assunto

    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

class Grupo(models.Model):
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=256, blank=True, null=True)

    nome = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.ImageField(upload_to=caminho)
    mapa = models.TextField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3974.278131225411!2d-42.80071524911858!3d-5.058599352781233!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x77c4de0a93d78d1%3A0xfcf5d4a169075b0!2sUniversidade%20Federal%20do%20Piau%C3%AD!5e0!3m2!1spt-BR!2sbr!4v1589396552722!5m2!1spt-BR!2sbr', blank=True, null=True)
    telefone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    endereco = models.CharField(max_length=256, blank=True, null=True)
    facebook = models.CharField(max_length=256, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
    instagram = models.CharField(max_length=256, blank=True, null=True)
    
    informacoes = models.ManyToManyField(Informacao)
    pesquisadores = models.ManyToManyField(Pesquisador)
    instituicoes = models.ManyToManyField(Instituicao)
    linhas = models.ManyToManyField(Linha)
    servicos = models.ManyToManyField(Servico)
    publicacoes = models.ManyToManyField(Publicacao)
    premiacoes = models.ManyToManyField(Premiacao)
    portifolio = models.ManyToManyField(Portifolio)
    projetos = models.ManyToManyField(Projeto)
    formularios = models.ManyToManyField(Formulario)
    inscritos = models.ManyToManyField(Inscrito)
    newsletters = models.ManyToManyField(Newsletter)

    imagem_infraestrutura1 = models.ImageField(upload_to=caminho)
    imagem_infraestrutura2 = models.ImageField(upload_to=caminho)
    imagem_infraestrutura3 = models.ImageField(upload_to=caminho)
    
    def __str__(self):
        return self.responsavel.username

    class Meta():
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
