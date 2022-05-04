from django.contrib.auth.models import User
from app_animals.models import Animal
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    animals = serializers.PrimaryKeyRelatedField(many=True, queryset=Animal.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'animals']
