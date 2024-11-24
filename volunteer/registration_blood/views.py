from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import DonorRegistration
from .serializers import DonorRegistrationSerializer, DonorRegistrationCreateSerializer
from rest_framework.permissions import IsAuthenticated

class DonorRegistrationViewSet(viewsets.ModelViewSet):
    queryset = DonorRegistration.objects.all()
    serializer_class = DonorRegistrationSerializer
    permission_classes = [IsAuthenticated]  # Đảm bảo người dùng đã đăng nhập

    # Tùy chỉnh truy vấn nếu cần (ví dụ: lọc theo người hiến máu hoặc sự kiện)
    def get_queryset(self):
        queryset = DonorRegistration.objects.all()
        donor_id = self.request.query_params.get('donor_id', None)
        event_id = self.request.query_params.get('event_id', None)
        if donor_id is not None:
            queryset = queryset.filter(donor_id=donor_id)
        if event_id is not None:
            queryset = queryset.filter(event_id=event_id)
        return queryset

        # Override the create method to customize POST request

    @swagger_auto_schema(
        request_body=DonorRegistrationCreateSerializer,
        responses={201: DonorRegistrationCreateSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = DonorRegistrationCreateSerializer(data=request.data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Perform custom actions here (e.g., logging, additional validation, etc.)

            # Save the instance and get the response data
            instance = serializer.save()

            # You can add custom success messages or logic here
            return Response(
                self.get_serializer(instance).data,
                status=status.HTTP_201_CREATED
            )
        else:
            # Return validation errors if serializer is not valid
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(request_body=no_body)
    @action(detail=True, methods=['put'], url_name='cancel')
    def cancel(self, request, pk=None):
        try:
            # Lấy đối tượng sự kiện cần hủy
            instance = self.get_object()

            # Thay đổi trạng thái của sự kiện (hoặc đăng ký)
            instance.status = "cancelled"
            instance.save()

            return Response(
                {"message": "Trạng thái sự kiện đã được hủy thành công."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"Không thể hủy sự kiện: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
