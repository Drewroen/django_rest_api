from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Event
from .serializers import UserSerializer, EventSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    resource_name = 'events'
    queryset = Event.objects.all().order_by('-time')
    serializer_class = EventSerializer