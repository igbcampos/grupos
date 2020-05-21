from django.urls import path
from .views import inicio, logar, deslogar, grupo

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login', logar, name='login'),
    path('logout', deslogar, name='logout'),

    path('<grupo>', grupo, name='grupo'),
]