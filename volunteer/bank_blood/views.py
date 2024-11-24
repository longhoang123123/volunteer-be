from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BloodBank
from .serializers import BloodBankSerializer
from datetime import date

class BloodBankViewSet(viewsets.ModelViewSet):
   
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer

    @action(detail=False, methods=['get'], url_path='expired', url_name='expired_blood')
    def expired_blood(self, request):

        expired_blood = self.queryset.filter(expiry_date__lt=date.today())
        serializer = self.get_serializer(expired_blood, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='in-stock', url_name='in_stock_blood')
    def in_stock_blood(self, request):

        in_stock_blood = self.queryset.filter(status='In Stock')
        serializer = self.get_serializer(in_stock_blood, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], url_path='update-quantity', url_name='update_quantity')
    def update_quantity(self, request, pk=None):

        blood = self.get_object()
        new_quantity = request.data.get('quantity', None)
        if new_quantity is not None:
            try:
                blood.quantity = int(new_quantity)
                blood.save()
                return Response({'detail': 'Quantity updated successfully.'}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({'detail': 'Invalid quantity value.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Quantity not provided.'}, status=status.HTTP_400_BAD_REQUEST)
