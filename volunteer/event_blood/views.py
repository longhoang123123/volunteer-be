from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BloodDonationEvent
from .serializers import BloodDonationEventSerializer

class BloodDonationEventViewSet(viewsets.ModelViewSet):
    queryset = BloodDonationEvent.objects.all()
    serializer_class = BloodDonationEventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
