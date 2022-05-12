from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Animal
        fields = '__all__'
