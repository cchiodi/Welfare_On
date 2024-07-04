from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'logs', LogViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
