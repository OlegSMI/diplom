from rest_framework.response import Response

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

    def get(self, request):
        posts = request.get(f'http://127.0.0.1:8888/user/posts/?user={id}')
        comments_1 = request.get(f'http://127.0.0.1:8888/user/posts/comments/?owner_comment_text={id}')
        comments_2 = request.get(f'http://127.0.0.1:8888/groups/comments/user/?owner_comment_text={id}')
        groups = request.get(f'http://127.0.0.1:8888/groups/user/?group_user={id}')

        # friends and info about this user
        infouser = request.get(f'http://127.0.0.1:8888/user/get_info/{id}')
        print(posts)

        return Response({"posts": posts})


