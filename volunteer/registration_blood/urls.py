from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonorRegistrationViewSet

router = DefaultRouter()
router.register(r'donor-registrations', DonorRegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
