from rest_framework import viewsets
from .models import User, Log
from .serializers import UserSerializer, LogSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class LogViewSet(viewsets.ModelViewSet):
	queryset = Log.objects.all()
	serializer_class = LogSerializer
