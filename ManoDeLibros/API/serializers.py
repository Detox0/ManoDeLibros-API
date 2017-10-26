from .models import *
from rest_framework import serializers

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
        fields = ('id', 'titulo', 'autor', 'ano', 'genero', 'precio', 'descripcion', 'editorial', 'autor')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'porcentaje', 'dealer', 'lector')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        depth = 1
        fields = ('id', 'nombre', 'region')

class DireccionSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer()
    class Meta:
        model = Direccion
        
        fields = ('id', 'calle', 'numero', 'ciudad')

class DealerSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()
    class Meta:
        model = Dealer
        fields = ('id', 'nombre', 'fono', 'correo', 'contrasena', 'direccion')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'nombre')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id', 'tipo')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre')

class Dealer_CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer_Catalogo
        fields = ('id', 'dealer', 'libro')

class Pedido_LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Lector
        fields = ('id', 'pedido', 'lector')

class Pedido_LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Libro
        fields = ('id','pedido','libro')