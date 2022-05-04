from django.urls import path
from app_users.views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='users_detail' ),
]