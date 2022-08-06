from rest_framework import viewsets
from pedidos.models import pedido, estadoAtual
from pedidos.serializer import PedidoSerializer, estadoAtualserializer

class pedidosViewSet(viewsets.ModelViewSet):
     """exibindo pedidos e comandas"""    
serializer_class = PedidoSerializer     
queryset = pedido.objects.all()


class estadoAtualViewSet(viewsets.ModelViewSet):
    """exibindo o estado"""
queryset = estadoAtual.objects.all()
serializer_class = estadoAtualserializer
