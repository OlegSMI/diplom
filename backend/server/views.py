from traceback import print_list
from rest_framework.response import Response
import requests

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .models import InfoUser
from .serializers import InfoUserSerializer

from .service_func.distance import distance_hamming

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
        mass = []

        users = requests.get('http://127.0.0.1:8888/user/all_users/')
        keywords = [
                    'agressor',
                    'military',
                    'ukraine',
                    'situation',
                    'toworrow',
                    'equipment',
                    'armor',
                    'attack',
                    'russia',
                    'america',
                    'country',
                    'green'
                    ]   
        for user in users.json():
            for user_com in user['comments_group']:
                for key in keywords:
                    if any([distance_hamming(i.lower(), key)<3 for i in user_com['comment_text'].split()]):
                        if user not in mass:
                            mass.append(user)
            for user_post in user['posts']:
                for key in keywords:
                    if any([distance_hamming(i.lower(), key)<3 for i in user_post['post_text'].split()]):
                        if user not in mass:
                            mass.append(user)
            for user_com in user['comments']:
                for key in keywords:
                    if any([distance_hamming(i.lower(), key)<3 for i in user_com['comment_text'].split()]):
                        if user not in mass:
                            mass.append(user)
           
        return Response(mass)

        