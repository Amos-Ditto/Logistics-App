from drf_yasg import openapi

response_schema_dict = {
    "201": openapi.Response(
        description="Htpp 201 description",
        examples={
            "application/json": {
                "key": "value",
            }
        },
    ),
    "500": openapi.Response(
        description="Htpp 500 description",
        examples={
            "application/json": {
                "key_1": "error message 1",
                "key_2": "error message 2",
            }
        },
    ),
}
