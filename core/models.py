from django.db import models
from django.contrib.auth.models import User


# Documentos

class Documento(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    data = models.DateField(null=True, blank=True)     
    def __str__(self):
        return self.nome + ' - ' + self.data

# Idiomas

class Idioma(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

# Tema

class Tema(models.Model):
    cor_destaque = models.CharField(max_length=256, blank=True, null=True)
    cor_um = models.CharField(max_length=256, blank=True, null=True)
    cor_dois = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.cor_destaque

    class Meta():
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

# Sobre

class Sobre(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    mapa = models.TextField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3974.278131225411!2d-42.80071524911858!3d-5.058599352781233!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x77c4de0a93d78d1%3A0xfcf5d4a169075b0!2sUniversidade%20Federal%20do%20Piau%C3%AD!5e0!3m2!1spt-BR!2sbr!4v1589396552722!5m2!1spt-BR!2sbr', blank=True, null=True)
    telefone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    endereco = models.CharField(max_length=256, blank=True, null=True)
    facebook = models.CharField(max_length=256, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
    instagram = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

# Pesquisador

class Pesquisador(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    descricao_completa = models.TextField(max_length=300, blank=True, null=True)
    lattes = models.CharField(max_length=256, blank=True, null=True)
    orcid = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Pesquisador'
        verbose_name_plural = 'Pesquisadores'

# Instituição

class Instituicao(models.Model):
    categorias = [('Nacional', 'Nacional'), ('Internacional', 'Internacional')]

    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    categoria = models.CharField(max_length=256, blank=True, null=True, choices=categorias)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Parceiros/Colaboradores'
        verbose_name_plural = 'Parceiros/Colaboradores'

# Linha de Pesquisa

class Linha(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    imagem = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Linha de Pesquisa'
        verbose_name_plural = 'Linhas de Pesquisa'

# Serviço

class Servico(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

# Publicação

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

# Premiação

class Premiacao(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    ano = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Premiação'
        verbose_name_plural = 'Premiações'

# Portifolio

class Portifolio(models.Model):
    nome = models.CharField(max_length=256, blank=True, null=True)
    descricao = models.CharField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Portifolio'
        verbose_name_plural = 'Portifolios'

#Projeto
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
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    sobre = models.ForeignKey(Sobre, on_delete=models.CASCADE)
    pesquisadores = models.ManyToManyField(Pesquisador)
    instituicoes = models.ManyToManyField(Instituicao)
    linhas = models.ManyToManyField(Linha)
    servicos = models.ManyToManyField(Servico)
    publicacoes = models.ManyToManyField(Publicacao)
    premiacoes = models.ManyToManyField(Premiacao)
    portifolio = models.ManyToManyField(Portifolio)
    projetos = models.ManyToManyField(Projeto)
    imagem_infraestrutura1 = models.CharField(max_length=256, blank=True, null=True)
    imagem_infraestrutura2 = models.CharField(max_length=256, blank=True, null=True)
    imagem_infraestrutura3 = models.CharField(max_length=256, blank=True, null=True)
    descricao_infraestrutura = models.TextField(max_length=1024, blank=True, null=True)
    
    def __str__(self):
        return self.sobre.nome

    class Meta():
        verbose_name = 'Informação'
        verbose_name_plural = 'Informações'

class Grupo(models.Model):
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    informacoes = models.ManyToManyField(Informacao)
    url = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.responsavel.username

    class Meta():
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
