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

urlpatterns = [
    path('users', views.UserListView.as_view()),
    path('users/<int:num_user>', views.MilitaryOneUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]