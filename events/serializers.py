from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Event
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'groups')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'