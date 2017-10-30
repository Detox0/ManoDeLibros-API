# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dealer, Libro, Genero, Region, Direccion, Autor
from .serializers import DealerSerializer, LibroSerializer, GeneroSerializer, RegionSerializer, DireccionSerializer, AutorSerializer, Dealer_CatalogoSerializer
import json

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
