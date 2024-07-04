from rest_framework import serializers
from .models import Service, UserService
from categories.serializers import SubcategorySerializer


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'


class UserServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserService
		fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
	subcategory_name = serializers.CharField(source='subcategory.name')
	category_id = serializers.IntegerField(source='subcategory.category.id')
	category_name = serializers.CharField(source='subcategory.category.name')
	category_color = serializers.CharField(source='subcategory.category.color')

	class Meta:
		model = Service
		fields = '__all__'
