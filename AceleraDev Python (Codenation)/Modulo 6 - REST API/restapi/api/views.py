from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.http import HttpResponse, HttpRequest
from rest_framework.parsers import JSONParser,ParseError
import datetime
import json
from django.http import JsonResponse


# Create your views here.

#Exemplo da doc
@api_view(['GET'])
def current_datetime(request):
    if request.method == 'GET':

        now = datetime.datetime.now()

        return Response(now)


@api_view(['POST'])
def hello_world(request):

    data = request.data['question']

    sorted_data = data.sort()

    json_answer = {"solution": sorted_data}

    return Response(json_answer)




