from .serializers import BigSerializer

def dict_serializer(model):
    information = {}
    information['infouser'] = model
    information['groups'] = model.group_key.all()
    information['friends'] = model.friends_key.all()
    information['posts'] = model.posts_key.all()
    information['comments'] = model.comments_key.all()
    information['geolocation'] = model.geolocation_key.all()
    serializer = BigSerializer(information)
    return serializer.data