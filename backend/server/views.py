from traceback import print_list
from rest_framework.response import Response
import requests

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .models import InfoUser
from .serializers import InfoUserSerializer

class UserListView(ListCreateAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer

class MilitaryOneUser(RetrieveAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer
    lookup_field = 'num_user'
    

class GetUserInfoInSosialNetwork(APIView):

    def get(self, request, id=1):
        posts = requests.get(f'http://127.0.0.1:8888/user/posts/?user={id}')
        comments_1 = requests.get(f'http://127.0.0.1:8888/user/posts/comments/?owner_comment_text={id}')
        comments_2 = requests.get(f'http://127.0.0.1:8888/groups/comments/user/?owner_comment_text={id}')
        groups = requests.get(f'http://127.0.0.1:8888/groups/user/?group_user={id}')
        infouser = requests.get(f'http://127.0.0.1:8888/user/get_info/{id}')
        
        return Response({
            "infouser": infouser.json(),
            "posts": posts.json(),
            "groups": groups.json(),
            "comments": comments_1.json()+comments_2.json(),
        })


class GetAllUserInfoInSosialNetwork(APIView):
    
    def get(self, request):

        