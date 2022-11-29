from drf_yasg import openapi
from .serializers import DeliveryManagerSerializer, UserSerializer

registration_response_schema = {
    200: UserSerializer(many=False),
    400: openapi.Response(
        description="Http 400 Error `Bad Request` description",
        examples={"application/json": {"field": ["error message."]}},
    ),
}

login_response_schema = {
    200: UserSerializer(many=False),
    400: openapi.Response(
        description="Http 400 Error `Bad Request` description",
        examples={"application/json": {"field": ["error message."]}},
    ),
    401: openapi.Response(
        description="Http 401 Error description",
        examples={"application/json": {"Error": "You entered the wrong credentials"}},
    ),
    500: openapi.Response(
        description="Http 401 Error description",
        examples={
            "application/json": {
                "Error": "User with the following Email does not exist"
            }
        },
    ),
}


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

post_managers_response_schema = {
    200: DeliveryManagerSerializer(many=False),
    500: openapi.Response(
        description="Http internal server Error description",
        examples={
            "application/json": {
                "Error": "The station id doesn't exist yet",
            }
        },
    ),
    401: openapi.Response(
        description="Http 401 Error description",
        examples={
            "application/json": {
                "Error": "User with this email doesn't exist yet",
            }
        },
    ),
    400: openapi.Response(
        description="Http 400 Bad Request Error description",
        examples={"application/json": {"field": ["error message."]}},
    ),
}
