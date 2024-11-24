from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.models import User
from app.serializers import UserSerializer, UserVerifySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=UserVerifySerializer)
    @action(methods=['POST'], detail=False, url_path='verify-email')
    def verify_email(self, request, *args, **kwargs):
        serializer = UserVerifySerializer(data=request.data)
        serializer.validate(attrs=request.data)
        return Response("Xác minh thành công.", status=status.HTTP_200_OK)
