from rest_framework import routers,serializers,viewsets
from .models import *

class InfoUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfoUser
        fields = ['num_user', 'user_id', 'name', 'online_status', 'status', 'photo', 'town', 'languages']

class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['groups']

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friends
        fields = ['friends']

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['posts']

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['comments']

class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['location']

class BigSerializer(serializers.Serializer):
    infouser=InfoUserSerializer(read_only=True)
    groups=UserGroupSerializer(read_only=True, many=True)
    friends=FriendsSerializer(read_only=True, many=True)
    posts=PostsSerializer(read_only=True, many=True)
    comments=CommentsSerializer(read_only=True, many=True)
    geolocation=GeolocationSerializer(read_only=True, many=True)

