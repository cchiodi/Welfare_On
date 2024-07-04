from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Service, UserService
from .serializers import ServiceSerializer, UserServiceSerializer, ServiceDetailSerializer


class ServiceViewSet(viewsets.ModelViewSet):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	@action(detail=False, methods=['get'])
	def detailed(self, request):
		services = Service.objects.all()
		serializer = ServiceDetailSerializer(services, many=True)
		return Response(serializer.data)

	@action(detail=False, methods=['get'])
	def filtered_detailed(self, request):
		category_id = request.query_params.get('id')
		if category_id:
			services = Service.objects.filter(subcategory__category_id=category_id)
			serializer = ServiceDetailSerializer(services, many=True)
			return Response(serializer.data)
		return Response({"detail": "category id not provided"}, status=400)


class UserServiceViewSet(viewsets.ModelViewSet):
	queryset = UserService.objects.all()
	serializer_class = UserServiceSerializer
