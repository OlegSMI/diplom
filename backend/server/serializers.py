from rest_framework import serializers
from .models import InfoUser, Posts, UserGroup, Friends, Comments, Geolocation

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'posts')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('id', 'groups')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('id', 'friends')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'comments')

class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('id', 'location')


class InfoUserSerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)
    comments = CommentsSerializer(many=True)
    friends = FriendsSerializer(many=True)
    groups = GroupSerializer(many=True)
    geolocation = GeolocationSerializer(many=True)

    class Meta:
        model = InfoUser
        fields = (  'num_user', 'user_id', 'name', 
                    'online_status', 'status', 'photo',
                    'town', 'languages', 'posts',
                    'comments', 'friends', 'groups',
                    'geolocation'
                    )







