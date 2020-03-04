from django.db import models
from django.contrib.auth.models import User

# Idiomas

class Idioma(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)

# Tema

class Tema(models.Model):
    cor_destaque = models.CharField(max_length=256, blank=True, null=True)
    cor_um = models.CharField(max_length=256, blank=True, null=True)
    cor_dois = models.CharField(max_length=256, blank=True, null=True)

# Sobre

class Sobre(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    telefone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    endereco = models.CharField(max_length=256, blank=True, null=True)
    facebook = models.CharField(max_length=256, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
    instagram = models.CharField(max_length=256, blank=True, null=True)

# Pesquisador

class Pesquisador(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    lattes = models.CharField(max_length=256, blank=True, null=True)

# Instituição

class Instituicao(models.Model):
    categorias = [('Nacional', 'Nacional'), ('Internacional', 'Internacional')]

    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    categoria = models.CharField(max_length=256, blank=True, null=True, choices=categorias)

# Linha de Pesquisa

class Linha(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)

# Publicação

class Publicacao(models.Model):
    categorias = [('Livro', 'Livro'), ('Journal Papers', 'Journal Papers'), ('Conference Papers', 'Conference Papers'), ('Keynote Speaches', 'Keynote Speaches'), ('Outro', 'Outro')]

    nome = models.CharField(max_length=256, blank=True, null=True)
    ano = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    categoria = models.CharField(max_length=256, blank=True, null=True, choices=categorias)

# Premiação

class Premiacao(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    ano = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)

# Projeto

class Projeto(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)

class Informacao(models.Model):
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    sobre = models.ForeignKey(Sobre, on_delete=models.CASCADE)
    pesquisadores = models.ManyToManyField(Pesquisador, on_delete=models.CASCADE)
    instituicao = models.ManyToManyField(Instituicao, on_delete=models.CASCADE)
    linhas = models.ManyToManyField(Linha, on_delete=models.CASCADE)
    publicacoes = models.ManyToManyField(Publicacao, on_delete=models.CASCADE)
    premiacoes = models.ManyToManyField(Premiacao, on_delete=models.CASCADE)
    projetos = models.ManyToManyField(Projeto, on_delete=models.CASCADE)

class Grupo(models.Model):
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    informacoes = models.ManyToManyField(Informacao, on_delete=models.CASCADE)
