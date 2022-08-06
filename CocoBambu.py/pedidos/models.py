from pyexpat import model
from sqlite3 import Timestamp
from django.db import models

class pedido (models.Model):
    cliente = models.CharField(max_length=30)
    produto = models.CharField(max_length=30)
    valor = models.CharField(max_length=6)
    entregue = models.BooleanField()
    estado = models.CharField(max_length=10)
    Timestamp = models.DateTimeField()

    def __str__(self):
     return self.cliente

class estadoAtual (models.Model):
    NIVEL = (
        ('1', 'RECEIVED'),
        ('2', 'CONFIRMED'),
        ('3', 'DISPATCHED'),
        ('4', 'DELIVERED'),
        ('5', 'CANCELED')
    )
    
    nivel=models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='4')
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nivel