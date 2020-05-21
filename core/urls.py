from django.urls import path
from .views import inicio, grupo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('<grupo>', grupo, name='grupo'),
]