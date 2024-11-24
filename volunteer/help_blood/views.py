from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BloodRecipient
from .serializers import BloodRecipientSerializer

class BloodRecipientListCreateView(generics.ListCreateAPIView):

    queryset = BloodRecipient.objects.all()
    serializer_class = BloodRecipientSerializer
    permission_classes = [IsAuthenticated]

class BloodRecipientDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BloodRecipient.objects.all()
    serializer_class = BloodRecipientSerializer
    permission_classes = [IsAuthenticated]
