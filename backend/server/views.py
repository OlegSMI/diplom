# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from .models import InfoUser
from .serializers import InfoUserSerializer

class UserListView(ListCreateAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer

class MilitaryOneUser(RetrieveAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer
    lookup_field = 'num_user'
    
class CommentsView(CreateAPIView):
    queryset = request.get('http://127.0.0.1:8888/groups/comments/')
