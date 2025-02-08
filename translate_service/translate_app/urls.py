# create urls for the app
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Microservice API Documentation",
        default_version="v1",
        description="API documentation for the Microservice backend",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # JSON schema
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('translate/', views.TranslateView.as_view(), name='translate'),
    # add ge_data to the path of the app as post method to get data from the user
    path('getdata/', views.GetTranslateView.as_view(), name='get_data'),
    # add likeorunlike to the path of the app as post method to get data from the user
    path('likeorunlike/', views.UpdateTranslateView.as_view(), name='like_or_unlike'),
    # add suggest to the path of the app as post method to get data from the user
    path('suggest/', views.SuggetsTranslateView.as_view(), name='suggest')
]