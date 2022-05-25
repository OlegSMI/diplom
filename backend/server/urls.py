# from django.urls import path 
# from . import views

# urlpatterns = [
#     path('', views.ListView.as_view()),
#     # path('about/', views.about),
#     path('detail/<int:pk>', views.MilitaryOneUser.as_view()),
#     # path('map/', views.geolocation),
# ]


from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.ListView, basename='allusers')
router.register(r'users/<int:pk>', views.MilitaryOneUser, basename='oneuser')

urlpatterns = [
    path('', include(router.urls)),
    path('users', views.ListView.as_view()),
    path('users/<int:pk>', views.MilitaryOneUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]