from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, UserServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'user_services', UserServiceViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('services/detailed/', ServiceViewSet.as_view({'get': 'detailed'})),
	path('services/filtered_detailed/', ServiceViewSet.as_view({'get': 'filtered_detailed'}))
]
