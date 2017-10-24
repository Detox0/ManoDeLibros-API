from .models import *
from rest_framework import serializers

class DealerSerializer(serializers.ModelSerializer):
    class Meta:

        model = Dealer
        fields = ('id', 'nombre', 'lugar', 'fono', 'correo', 'contrasena')


class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = ('id', 'nombre', 'sexo', 'correo')


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'fecha', 'total', 'estado', 'dealer', 'lector')


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('id', 'nombre', 'lugar', 'correo', 'contrasena')


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'ano', 'genero', 'precio', 'descripcion', 'editorial', 'pedido')


class ComisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comision
        fields = ('id', 'porcentaje', 'envio', 'pedido')


class Ratingerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'porcentaje', 'dealer', 'lector')


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id', 'nombre')


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'nombre')