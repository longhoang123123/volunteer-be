from django.urls import path
from . import views

urlpatterns = [
    path('recipients/', views.BloodRecipientListCreateView.as_view(), name='recipient-list-create'),
    path('recipients/<int:pk>/', views.BloodRecipientDetailView.as_view(), name='recipient-detail'),
]
