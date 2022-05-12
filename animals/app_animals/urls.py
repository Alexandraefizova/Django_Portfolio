from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<int:pk>/', AnimalsDetailView.as_view(), name='detail'),
    path('add/', CreateAnimals.as_view(), name='add_animals'),
    path('delete/', delete_animals, name='delete'),
]