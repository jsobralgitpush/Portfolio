from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Projeto Final import con

#Aqui vai ser onde vou criar os endpoints
@api_view(['GET'])
def get_users(request):

