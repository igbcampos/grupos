from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, logar, deslogar, administracao, newsletter, criar_newsletter, grupo, inscrever

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('administracao', administracao, name='administracao'),
    path('newsletter', newsletter, name='newsletter'),
    path('newsletter/criar', criar_newsletter, name='criar_newsletter'),

    path('<sigla>/<idioma>', grupo, name='grupo'),
    path('<sigla>/<idioma>/inscrever', inscrever, name='inscrever'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)