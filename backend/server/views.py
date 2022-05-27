# from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from .dictserializer import dict_serializer

from loguru import logger

class UserListView(ListCreateAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer

class MilitaryOneUser(RetrieveAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer
    lookup_field = 'num_user'


# def parse_detail(request, pk):
#     model = InfoUser.objects.get(pk=pk)
#     if(request.method == 'PUT'):
#         data = JSONParser().parse(request)  
#         serializer = InfoUserSerializer(model, data=data)
#         if(serializer.is_valid()):  
#             serializer.save() 
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif(request.method == 'DELETE'):
#         model.delete() 
#         return HttpResponse(status=204) 

# @csrf_exempt
# def about(request):
#     pass

# @csrf_exempt
# def geolocation(request):
#     pass

