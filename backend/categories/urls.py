from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('subcategories/filter_by_category/', SubcategoryViewSet.as_view({'get': 'filter_by_category'})),
]
