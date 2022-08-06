from django.contrib import admin
from pedidos.models import pedido, estadoAtual


class Pedidos(admin.ModelAdmin):
    list_display = ('id','cliente','produto', 'valor', 'estado','time')
    list_display_links = ('id', 'cliente')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(pedido)

class estadoAtual(admin.ModelAdmin):
    list_display = ('1','2','3','4','5')
    list_display_links = ('cliente')
    search_fields = ('cliente')
    list_per_page = 20
    