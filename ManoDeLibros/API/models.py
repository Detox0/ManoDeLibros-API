from django.db import models
import datetime

class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=15)
    correo = models.EmailField()


class Dealer(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=50)
    fono = models.CharField(max_length=13)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)

class Pedido(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now)
    total = models.IntegerField()
    estado = models.CharField(max_length=15)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField(default=0)
    genero = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


class Comision(models.Model):
    porcentaje = models.FloatField()
    envio = models.IntegerField()
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)


class Rating(models.Model):
    porcentaje = models.FloatField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)

class Direccion(models.Model):
    nombre = models.CharField(max_length=100)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

class Region(models.Model):
    nombre = models.CharField(max_length=100)