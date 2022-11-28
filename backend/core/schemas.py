from drf_yasg import openapi
from .serializers import DeliveryManagerSerializer

get_managers_response_schema = {
    200: DeliveryManagerSerializer(many=False),
    401: openapi.Response(
        description="Http 401 Error description",
        examples={
            "application/json": {
                "Error": "Manager with this email Address doesn't exists",
            }
        },
    ),
}
