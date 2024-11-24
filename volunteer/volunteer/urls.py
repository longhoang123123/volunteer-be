from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your.email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Không cần include cho admin
    path('api/v1/', include('app.urls')),  # Đảm bảo 'app.urls' có tồn tại

    path('api/blood/', include('blood.urls')),

    path('api/v1/event_blood/', include('event_blood.urls')),

    path('api/v1/registration_blood/', include('registration_blood.urls')),

    path('api/v1/help_blood/', include('help_blood.urls')),


    path('api/v1/auth/', include('djoser.urls.jwt')),

    # Đường dẫn cho Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Đường dẫn cho tài liệu dưới dạng JSON
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
