from django.db import models
from datetime import datetime
from veiculo.consts import *

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS, verbose_name='Combustível')
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS, verbose_name='Marca')
    cor = models.SmallIntegerField(choices=OPCOES_CORES, verbose_name='Cor')
    ano = models.IntegerField(verbose_name='Ano')


    def __str__(self):
        return f'{self.modelo} - {self.placa}'

 