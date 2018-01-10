from django.db import models
import datetime

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#asdasd
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField(default=0)
    departamento = models.CharField(max_length=10, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=True, null=True)

class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=15)
    correo = models.EmailField(null=True, blank= True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Dealer(models.Model):
    nombre = models.CharField(max_length=100)
    fono = models.CharField(max_length=13)
    correo = models.EmailField(default='')
    contrasena = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null = True, blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now)
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=15)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)


class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(default='')
    contrasena = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    tipo = models.CharField(max_length = 50, unique=True)
    ventas = models.IntegerField(default=0)

    def __str__(self):
        return self.tipo

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    descripcion = models.TextField(default='')
    imagenURL = models.TextField(default='')
    fecha = models.DateField(default=datetime.datetime.now)
    venta = models.IntegerField(default=0)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Rating(models.Model):
    porcentaje = models.FloatField()
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)

class Dealer_Catalogo(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, blank=True, null=True)

class Pedido_Libro(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, blank=True, null=True)

class Pedido_Lector(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE, blank=True, null=True)