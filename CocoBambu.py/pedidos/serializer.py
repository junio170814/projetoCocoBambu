from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from pedidos.models import pedido, estadoAtual


class PedidoSerializer (serializers.ModelSerializer):
    class meta:
      model = pedido
      fields = ['id', 'cliente', 'produto', 'valor', 'estado', 'timestamp']

class estadoAtualserializer (serializers.ModelSerializer):
    class meta:
        model = estadoAtual
        fields = ['__all__']
