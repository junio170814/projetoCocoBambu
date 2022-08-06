from django.contrib import admin
from django.db import router
from django.urls import path, include
from pedidos.views import pedidosViewSet, estadoAtualViewSet
from rest_framework import routers
from pedidos.admin import Pedidos

router = routers.DefaultRouter()
router.register('pedido', pedidosViewSet, basename='Pedido')
router.register('estado', estadoAtualViewSet, basename='estado')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
