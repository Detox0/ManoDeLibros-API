# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(Editorial)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Dealer)
admin.site.register(Lector)
admin.site.register(Libro)
admin.site.register(Direccion)
admin.site.register(Pedido)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Dealer_Catalogo)

