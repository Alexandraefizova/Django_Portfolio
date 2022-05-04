from django.urls import path
from app_animals.views import AnimalsList, AnimalsDetail

urlpatterns = [
    path('animals/', AnimalsList.as_view(), name='animals_list'),
    path('animals/<int:pk>/', AnimalsDetail.as_view(), name='animals_detail' ),
]