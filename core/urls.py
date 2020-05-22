from django.urls import path
from .views import inicio, logar, deslogar, administracao, newsletter, criar_newsletter, grupo, inscrever

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('administracao', administracao, name='administracao'),
    path('newsletter', newsletter, name='newsletter'),
    path('newsletter/criar', criar_newsletter, name='criar_newsletter'),

    path('<sigla>', grupo, name='grupo'),
    path('<sigla>/inscrever', inscrever, name='inscrever'),
]