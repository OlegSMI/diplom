from django.urls import include, path
from . import views

urlpatterns = [
    path('users', views.UserListView.as_view()),
    path('users/<int:num_user>', views.MilitaryOneUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('data', views.GetUserInfoInSosialNetwork.as_view())
]