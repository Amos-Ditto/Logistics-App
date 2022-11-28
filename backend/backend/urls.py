from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomApiSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):

        swagger = super().get_schema(request, public)
        swagger.tags = [
            {"name": "User", "description": "Handles user Creation & Authentications"}
        ]
        return swagger


admin.site.ste_header = "Logistics Application Backend"
admin.site.index_title = "Backend"

schema_view = get_schema_view(
    openapi.Info(
        title="Logistics data source and API's",
        default_version="v1.0",
        description="APIs Doc",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="amosditto@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=CustomApiSchemaGenerator,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Open Api docs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Application urls
    path("api/", include("core.urls")),
    path("api/delivery", include("delivery.urls")),
]
