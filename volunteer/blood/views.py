# blood/views.py
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Donor
from .serializers import DonorSerializer, DonorCreateSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=DonorCreateSerializer)
    def create(self, request, *args, **kwargs):
        serializer = DonorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        method='GET',
        operation_summary="Get donor by user_id",
        operation_description="Retrieve donor information based on the provided user ID.",
        responses={
            200: "Donor information retrieved successfully.",
            404: "Donor not found.",
        }
    )
    @action(methods=['GET'], detail=False, url_path='users/(?P<user_id>[^/.]+)')
    def donors(self, request, user_id=None):
        """
        Custom action to get donor by user_id.
        """
        # Assuming you have a model named `Donor` and `user_id` is a field in it
        try:
            donor = Donor.objects.get(user_id=user_id)
            # Serialize the donor data
            serializer = DonorSerializer(donor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Donor.DoesNotExist:
            return Response(
                {"detail": "Donor not found."},
                status=status.HTTP_404_NOT_FOUND
            )