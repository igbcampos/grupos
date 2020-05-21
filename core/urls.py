from django.urls import path
from .views import inicio, logar, deslogar, administracao, grupo

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('administracao', administracao, name='administracao'),

    path('<grupo>', grupo, name='grupo'),
]