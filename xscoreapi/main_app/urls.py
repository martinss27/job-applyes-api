from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserApplicationViewSet

router = DefaultRouter()
router.register(r'user-applications', UserApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]