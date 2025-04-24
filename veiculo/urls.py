from django.contrib import admin
from django.urls import include, path

from veiculo.views import ListarVeiculos

urlpatterns = [
    path('listarVeiculos', ListarVeiculos.as_view(), name='listar_veiculos'),
]
