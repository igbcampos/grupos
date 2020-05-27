from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, logar, deslogar, administracao, salvar_sobre, salvar_pesquisador, copiar_pesquisador, excluir_pesquisador, salvar_instituicao, copiar_instituicao, excluir_instituicao, salvar_linha, copiar_linha, excluir_linha, salvar_servico, copiar_servico, excluir_servico, salvar_publicacao, copiar_publicacao, excluir_publicacao, salvar_premiacao, copiar_premiacao, excluir_premiacao, salvar_portifolio, copiar_portifolio, excluir_portifolio, salvar_projeto, copiar_projeto, excluir_projeto, newsletter, criar_newsletter, enviar_newsletter, grupo, formulario, inscrever

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('administracao', administracao, name='administracao'),
    path('administracao/salvar', administracao, name='salvar_administracao'),

    path('newsletter', newsletter, name='newsletter'),
    path('newsletter/criar', criar_newsletter, name='criar_newsletter'),
    path('newsletter/enviar', enviar_newsletter, name='enviar_newsletter'),

    path('sobre/salvar', salvar_sobre, name='salvar_sobre'),

    path('pesquisadores/<idioma>/salvar', salvar_pesquisador, name='salvar_pesquisador'),
    path('pesquisadores/<idioma>/salvar/<pk>', salvar_pesquisador, name='salvar_pesquisador'),
    path('pesquisadores/<idioma>/copiar', copiar_pesquisador, name='copiar_pesquisador'),
    path('pesquisadores/excluir/<pk>', excluir_pesquisador, name='excluir_pesquisador'),
    
    path('instituicoes/<idioma>/salvar', salvar_instituicao, name='salvar_instituicao'),
    path('instituicoes/<idioma>/salvar/<pk>', salvar_instituicao, name='salvar_instituicao'),
    path('instituicoes/<idioma>/copiar', copiar_instituicao, name='copiar_instituicao'),
    path('instituicoes/excluir/<pk>', excluir_instituicao, name='excluir_instituicao'),
    
    path('linhas/<idioma>/salvar', salvar_linha, name='salvar_linha'),
    path('linhas/<idioma>/salvar/<pk>', salvar_linha, name='salvar_linha'),
    path('linhas/<idioma>/copiar', copiar_linha, name='copiar_linha'),
    path('linhas/excluir/<pk>', excluir_linha, name='excluir_linha'),
    
    path('servicos/<idioma>/salvar', salvar_servico, name='salvar_servico'),
    path('servicos/<idioma>/salvar/<pk>', salvar_servico, name='salvar_servico'),
    path('servicos/<idioma>/copiar', copiar_servico, name='copiar_servico'),
    path('servicos/excluir/<pk>', excluir_servico, name='excluir_servico'),
    
    path('publicacoes/<idioma>/salvar', salvar_publicacao, name='salvar_publicacao'),
    path('publicacoes/<idioma>/salvar/<pk>', salvar_publicacao, name='salvar_publicacao'),
    path('publicacoes/<idioma>/copiar', copiar_publicacao, name='copiar_publicacao'),
    path('publicacoes/excluir/<pk>', excluir_publicacao, name='excluir_publicacao'),
    
    path('premiacoes/<idioma>/salvar', salvar_premiacao, name='salvar_premiacao'),
    path('premiacoes/<idioma>/salvar/<pk>', salvar_premiacao, name='salvar_premiacao'),
    path('premiacoes/<idioma>/copiar', copiar_premiacao, name='copiar_premiacao'),
    path('premiacoes/excluir/<pk>', excluir_premiacao, name='excluir_premiacao'),
    
    path('portifolios/<idioma>/salvar', salvar_portifolio, name='salvar_portifolio'),
    path('portifolios/<idioma>/salvar/<pk>', salvar_portifolio, name='salvar_portifolio'),
    path('portifolios/<idioma>/copiar', copiar_portifolio, name='copiar_portifolio'),
    path('portifolios/excluir/<pk>', excluir_portifolio, name='excluir_portifolio'),
    
    path('projetos/<idioma>/salvar', salvar_projeto, name='salvar_projeto'),
    path('projetos/<idioma>/salvar/<pk>', salvar_projeto, name='salvar_projeto'),
    path('projetos/<idioma>/copiar', copiar_projeto, name='copiar_projeto'),
    path('projetos/excluir/<pk>', excluir_projeto, name='excluir_projeto'),
    
    path('<sigla>', grupo, name='grupo'),
    path('<sigla>/<idioma>', grupo, name='grupo'),
    path('<sigla>/formulario', formulario, name='formulario'),
    path('<sigla>/<idioma>/formulario', formulario, name='formulario'),
    path('<sigla>/inscrever', inscrever, name='inscrever'),
    path('<sigla>/<idioma>/inscrever', inscrever, name='inscrever'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)