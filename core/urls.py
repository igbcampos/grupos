from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, logar, deslogar, administracao, newsletter, criar_newsletter, enviar_newsletter, grupo, formulario, inscrever

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('administracao', administracao, name='administracao'),
    path('administracao/salvar', administracao, name='salvar_administracao'),

    path('newsletter', newsletter, name='newsletter'),
    path('newsletter/criar', criar_newsletter, name='criar_newsletter'),
    path('newsletter/enviar', enviar_newsletter, name='enviar_newsletter'),

    path('<sigla>', grupo, name='grupo'),
    path('<sigla>/<idioma>', grupo, name='grupo'),
    path('<sigla>/formulario', formulario, name='formulario'),
    path('<sigla>/<idioma>/formulario', formulario, name='formulario'),
    path('<sigla>/inscrever', inscrever, name='inscrever'),
    path('<sigla>/<idioma>/inscrever', inscrever, name='inscrever'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)