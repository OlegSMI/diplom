# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .dictserializer import dict_serializer

from loguru import logger

class ListView(APIView):
    def get(self, request):
        model = InfoUser.objects.all()
        context = {}
        for i in model:
            data = dict_serializer(i)
            context[str(i)]=data
        return JsonResponse(context, status=201)

    @classmethod
    def get_extra_actions(cls):
        return []

class MilitaryOneUser(APIView):
 
    def get(self, request, pk):
        model = InfoUser.objects.get(pk=pk)
        data = dict_serializer(model)
        return JsonResponse(data, status=201)

    @classmethod
    def get_extra_actions(cls):
        return []


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

