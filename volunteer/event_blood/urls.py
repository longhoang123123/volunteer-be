from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BloodDonationEventViewSet

router = DefaultRouter()
router.register(r'events', BloodDonationEventViewSet, basename='event')  # Đăng ký ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Sử dụng router để tự động xử lý URL
]
