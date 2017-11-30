# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dealer, Libro, Genero, Region, Direccion, Autor
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import json
import hmac
import hashlib
import base64

#Retorna todos los dealers inscritos
def dealer_list(request):

    if request.method == 'GET':
        dealers = Dealer.objects.all()
        serializer = DealerSerializer(dealers, many=True)

        return JsonResponse(serializer.data, safe=False)


#Retorna todos los libros de la pagina
def libros_list(request):

    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna todos los generos de los libros inscritos
def genero_list(request):

    if request.method == 'GET':
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna todos las regiones inscritas
def region_list(request):

    if request.method == 'GET':
        regiones = Region.objects.all()
        serializer = RegionSerializer(regiones, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna todos las direcciones inscritas
def direccion_list(request):

    if request.method == 'GET':
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(direcciones, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna los autores registrados en la base de datos
def autor_list(request):

    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna los dealers de una ciudad en especifico
def dealer_city(request,ciudad):

    if request.method == 'GET':

        dealers = Dealer.objects.filter(direccion__ciudad__nombre = ciudad)
        serializer = DealerSerializer(dealers, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna los dealers de una region en especifico
def dealer_region(request,pk):

    if request.method == 'GET':

        dealers = Dealer.objects.filter(direccion__ciudad__region__id=pk)
        serializer = DealerSerializer(dealers, many=True)

        return JsonResponse(serializer.data, safe=False)

#Retorna todos los libros de un catálogo de un dealer
def dealer_catalogo(request, pk):

    if request.method == 'GET':

        id_libros = []
        selected_dealer = []
        dealers = Dealer.objects.filter(id=pk)
        serializer = DealerSerializer(dealers[0])
        selected_dealer.append(serializer.data)

        catalogos = Dealer_Catalogo.objects.filter(dealer=pk)
        for catalogo in catalogos:
            serializer =LibroSerializer(catalogo.libro)
            id_libros.append(serializer.data)

        return JsonResponse(id_libros, safe=False) #id_libros

#Retorna todos los libros de un pedido
def libros_pedido(request, pk):

    if request.method == 'GET':

        id_libros = []

        catalogos = Pedido_Libro.objects.filter(pedido=pk)

        for catalogo in catalogos:
            serializer =LibroSerializer(catalogo.libro)
            id_libros.append(serializer.data)

        return JsonResponse({'libros': id_libros})

#Funcion que retorna todas las Editoriales inscritas en la pagina
def all_editoriales(request):

    if request.method == 'GET':

        editoriales = Editorial.objects.all()

        serializer = EditorialSerializer(editoriales, many=True)

        return JsonResponse(serializer.data , safe= False)

# Funcion que se encarga de retornar a todos lo usuarios que poseen una contraseña
def all_users(request):

    if request.method == 'GET':
        usuarios_dealers = []
        usuarios_editoriales = []

        dealers = Dealer.objects.all()
        editoriales = Editorial.objects.all()

        for dealer in dealers:
            dealers_serializer = DealerSerializer(dealer)
            usuarios_dealers.append(dealers_serializer.data)

        for editorial in editoriales:
            editoriales_serializer = EditorialSerializer(editorial)
            usuarios_editoriales.append(editoriales_serializer.data)

        return JsonResponse({'dealers' : usuarios_dealers, 'editoriales' : usuarios_editoriales})

#Retorna todos los pedidos realizados
def all_pedidos(request):

    if request.method == 'GET':

        pedidos = Pedido.objects.all()

        serializer = PedidoSerializer(pedidos, many=True)

        return JsonResponse(serializer.data, safe=False)

def all_dealer_catalogos(request):

    if request.method == 'GET':
        
        catalogos = Dealer_Catalogo.objects.all()
        serializer = Dealer_CatalogoSerializer(catalogos, many=True)
        return JsonResponse(serializer.data, safe=False)

#Funcion que retorne los libros en base a su genero
def libros_genero(request,pk):

    if request.method == 'GET':

        libros = Libro.objects.filter(genero__id = pk)

        serializer = LibroSerializer(libros, many=True)

        return JsonResponse(serializer.data, safe=False)

#Funcion que retorna las ciudades de una region
def ciudades_region(request,pk):

    if request.method == 'GET':

        ciudades = Ciudad.objects.filter(region__id = pk)

        serializer = CiudadSerializer(ciudades, many=True)


        return JsonResponse(serializer.data, safe=False)


class catalogo_avanzado(generics.ListAPIView):
    queryset = Dealer_Catalogo.objects.all()
    serializer_class = Dealer_CatalogoSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('libro__titulo', 'libro__genero__tipo', 'libro__ano', 'libro__editorial__nombre', 'libro__autor__nombre')
    ordering_fields = ('id', 'libro__ano', 'libro__precio', 'libro__id', 'dealer__id')
    filter_fields = ('dealer__id', 'libro__id', 'dealer__direccion__ciudad__id', 'dealer__direccion__ciudad__nombre', 'dealer__direccion__ciudad__region__id')
    


class libros_avanzado(generics.ListAPIView):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer
	filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
	search_fields = ('titulo', 'genero__tipo', 'ano', 'editorial__nombre', 'autor__nombre')
	ordering_fields = ('id', 'ano', 'precio')
	filter_fields = ('id','autor__nombre','autor__id','genero__id','genero__tipo', 'ano', 'precio', 'editorial__nombre', 'editorial__id')
    
class dealer_avanzado(generics.ListAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('nombre', 'direccion__ciudad__region__nombre', 'direccion__ciudad__nombre')
    ordering_fields = ('direccion__ciudad__region__nombre', 'direccion__ciudad__nombre')
    filter_fields = ('id','direccion__ciudad__region__nombre', 'direccion__ciudad__region__id','direccion__ciudad__nombre', 'direccion__ciudad__id')

class pedido_avanzado(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('nombre', 'direccion__ciudad__region__nombre', 'direccion__ciudad__nombre', 'dealer__nombre')
    ordering_fields = ('fecha','estado')
    filter_fields = ('id','fecha','estado', 'dealer__id','dealer__nombre', 'dealer__direccion__ciudad__nombre', 'dealer__direccion__ciudad__region__nombre')

class pedido_Libro_avanzado(generics.ListAPIView):
    queryset = Pedido_Libro.objects.all()
    serializer_class = Pedido_LibroSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('libro__titulo', 'libro__editorial__nombre', 'libro__autor__nombre', 'libro__genero__tipo')
    ordering_fields = ('pedido__fecha','pedido_estado')
    filter_fields = ('id','pedido__id','pedido__fecha','pedido__estado', 'pedido__dealer__id','pedido__dealer__id','pedido__dealer__direccion__ciudad__id', 'pedido__dealer__direccion__ciudad__nombre', 'pedido__dealer__direccion__ciudad__region__nombre', 'pedido__dealer__direccion__ciudad__region__id')

class lector_avanzado(generics.ListAPIView):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('correo','nombre')
    ordering_fields = ('correo','nombre','id')
    filter_fields = ('correo','id')
    

#Funcion encargada de recibir un JSON con informacion de un autor e insertarlo en la base de datos
@csrf_exempt
def create_autor(request):

    if request.method == 'POST':

       data = JSONParser().parse(request)
       serializer = AutorSerializer(data=data)

       if serializer.is_valid():
           serializer.save()

           return JsonResponse(serializer.data, status=201)

       return JsonResponse(serializer.errors, status=400)

#Funcion encargada de recibir un JSON con informacion de un libro e insertarlo en la base de datos
@csrf_exempt
def create_libro(request):

    if request.method == 'POST':

       data = JSONParser().parse(request)
       serializer = LibroSerializer(data=data)

       if serializer.is_valid():
           serializer.save()

           return JsonResponse(serializer.data, status=201)

       return JsonResponse(serializer.errors, status=400)

#Funcion encargada de recibir un ID de dealer y un ID de libro y añadirlo a su catalogo

@csrf_exempt
def add_libro_catalogo(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = Dealer_CatalogoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

# Funcion encargada de crear un pedido
@csrf_exempt
def create_pedido(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = PedidoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

#Funcion encargada de crear un lector
@csrf_exempt
def create_lector(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = LectorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

#Funcion encargada de unir a un lector a un pedido
@csrf_exempt
def add_lector_pedido(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = Pedido_LectorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)



#Funcion encargada de recibir un libro y un pedido y unirlos
@csrf_exempt
def add_libro_pedido(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = Pedido_LibroSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def generar_pago(request,data_subject,pedido_id,data_amount,data_payer_email,data_notify_url,data_return_url, data_cancel_url):

    if request.method == 'GET':

        secret = 'e6733a41e12675fdd82b0fcde72e13862e2e5fdf'
        receiver_id = '154271'
        subject = data_subject
        body = ''
        amount = data_amount
        payer_email = data_payer_email
        bank_id ='' 
        expires_date = ''
        transaction_id = pedido_id
        custom = ''
        notify_url = data_notify_url
        return_url = data_return_url
        cancel_url = data_cancel_url
        picture_url = ''
        hash_data="receiver_id="+receiver_id+"&subject="+subject+"&body="+body+"&amount="+amount+"&payer_email="+payer_email+"&bank_id="+bank_id+"&expires_date="+expires_date+"&transaction_id="+transaction_id+"&custom="+custom+"&notify_url="+notify_url+"&return_url="+return_url+"&cancel_url="+cancel_url+"&picture_url="+picture_url
        hash_result = hmac.new(str(secret), str(hash_data), digestmod=hashlib.sha256).hexdigest()
        url = "https://khipu.com/api/1.3/createPaymentPage?receiver_id="+receiver_id+"&subject="+subject+"&body="+body+"&amount="+amount+"&notify_url="+notify_url+"&return_url="+return_url+"&cancel_url="+cancel_url+"&transaction_id="+transaction_id+"&expires_date="+expires_date+"&payer_email="+payer_email+"&custom="+custom+"&hash="+hash_result       
        
        return JsonResponse({'url_pago': url})
