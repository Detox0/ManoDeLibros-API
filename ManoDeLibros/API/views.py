# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dealer, Libro, Genero, Region
from .serializers import DealerSerializer, LibroSerializer, GeneroSerializer, RegionSerializer
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



