from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Subcategory
from .serializers import CategorySerializer, SubcategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
	queryset = Subcategory.objects.all()
	serializer_class = SubcategorySerializer

	@action(detail=False, methods=['get'])
	def filter_by_category(self, request):
		category_id = request.query_params.get('id')
		if category_id:
			subcategories = Subcategory.objects.filter(category_id=category_id)
			serializer = SubcategorySerializer(subcategories, many=True)
			return Response(serializer.data)
		return Response({"detail": "category id not provided"}, status=400)
