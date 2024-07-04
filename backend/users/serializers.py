from rest_framework import serializers
from .models import User, Log
from drf_writable_nested import WritableNestedModelSerializer
from services.serializers import UserServiceSerializer


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
	services = UserServiceSerializer(source='userservice_set', many=True)

	class Meta:
		model = User
		fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Log
		fields = '__all__'
