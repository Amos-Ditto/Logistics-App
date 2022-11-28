from drf_yasg import openapi
from drf_yasg.utils import guess_response_status
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import force_real_str, is_list_view
from rest_framework import exceptions
from rest_framework.settings import api_settings
from rest_framework import status


class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_responses(self):
        response_serializers = self.get_response_serializers()
        response_schemas = self.get_response_schemas(response_serializers)

        paginator = self.overrides.get("paginator", None)
        if paginator and self.has_list_response():
            method = self.method.lower()
            default_response_status = str(guess_response_status(method))
            if default_response_status in response_schemas:
                response_schemas[default_response_status] = openapi.Response(
                    description=response_schemas[default_response_status].description,
                    schema=self.get_paginated_response(
                        response_schemas[default_response_status].schema
                    ),
                )

        return openapi.Responses(responses=response_schemas)

    def get_paginated_response(self, response_schema):
        return self.probe_inspectors(
            self.paginator_inspectors,
            "get_paginated_response",
            self._get_paginator(),
            response_schema=response_schema,
        )

    def get_pagination_parameters(self):
        if not self.should_page():
            return []

        return (
            self.probe_inspectors(
                self.paginator_inspectors,
                "get_paginator_parameters",
                self._get_paginator(),
            )
            or []
        )

    def should_page(self):
        return self._get_paginator() and self.has_list_response()

    def _get_paginator(self):
        return self.overrides.get("paginator") or getattr(self.view, "paginator", None)

    def get_generic_error_schema(self):
        return openapi.Schema(
            "Generic API Error",
            type=openapi.TYPE_OBJECT,
            properties={
                "errors": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Error details"
                        ),
                        "code": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Error code"
                        ),
                    },
                )
            },
            required=["detail"],
        )

    def get_validation_error_schema(self):
        return openapi.Schema(
            "Validation Error",
            type=openapi.TYPE_OBJECT,
            properties={
                "errors": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="error messages for each field that triggered a validation error",
                    additional_properties=openapi.Schema(
                        description="A list of error messages for the field",
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                ),
                api_settings.NON_FIELD_ERRORS_KEY: openapi.Schema(
                    description="List of validation errors not related to any field",
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
        )

    def get_response_serializers(self):
        responses = super().get_response_serializers()
        definitions = self.components.with_scope(
            openapi.SCHEMA_DEFINITIONS
        )  # type: openapi.ReferenceResolver

        definitions.setdefault("GenericError", self.get_generic_error_schema)
        definitions.setdefault("ValidationError", self.get_validation_error_schema)
        definitions.setdefault("APIException", self.get_generic_error_schema)

        if self.get_request_serializer() or self.get_query_serializer():
            responses.setdefault(
                exceptions.ValidationError.status_code,
                openapi.Response(
                    description=force_real_str(
                        exceptions.ValidationError.default_detail
                    ),
                    schema=openapi.SchemaRef(definitions, "ValidationError"),
                ),
            )

        security = self.get_security()
        if security is None or len(security) > 0:
            # Note: 401 error codes are coerced  into 403 see rest_framework/views.py:433:handle_exception
            # This is b/c the API uses token auth which doesn't have WWW-Authenticate header
            responses.setdefault(
                status.HTTP_403_FORBIDDEN,
                openapi.Response(
                    description="Authentication credentials were invalid, absent or insufficient.",
                    schema=openapi.SchemaRef(definitions, "GenericError"),
                ),
            )
        if not is_list_view(self.path, self.method, self.view):
            responses.setdefault(
                exceptions.PermissionDenied.status_code,
                openapi.Response(
                    description="Permission denied.",
                    schema=openapi.SchemaRef(definitions, "APIException"),
                ),
            )
            responses.setdefault(
                exceptions.NotFound.status_code,
                openapi.Response(
                    description="Object does not exist or caller has insufficient permissions to access it.",
                    schema=openapi.SchemaRef(definitions, "APIException"),
                ),
            )

        return responses
