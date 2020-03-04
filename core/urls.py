from django.urls import path
from .views import inicio

urlpatterns = [
    path('<grupo>', inicio, name='inicio')
]