# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dealer
from .serializers import DealerSerializer
import json

#Retorna todos los dealers inscritos
def dealer_list(request):

    if request.method == 'GET':
        dealers = Dealer.objects.all()
        serializer = DealerSerializer(dealers, many=True)

        return JsonResponse(serializer.data, safe=False)


