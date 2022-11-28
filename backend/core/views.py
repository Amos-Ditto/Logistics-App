from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema, OrderedDict
from drf_yasg import openapi

from .serializers import UserSerializer, UserLoginSerializer

User = get_user_model()


class UserView(APIView):
    @swagger_auto_schema(
        tags=["User"],
        operation_description="Creates a new user based on the provided values. If desired an authentication JWT can be generated right away. After creating an account the initial group containing a database is created.",
        request_body=UserSerializer,
        responses={201: UserSerializer(many=False)},
    )
    def post(self, request):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            user = data.create(request.data)

            return Response(UserSerializer(user).data, status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    @swagger_auto_schema(
        tags=["User"],
        operation_description="Authenticates an existing user based on their email and their password. If successful, an access token and a refresh token will be returned.",
        request_body=UserLoginSerializer,
        responses={200: UserSerializer(many=False)},
    )
    def post(self, request):
        data = UserLoginSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.filter(
                emailAddress=request.data["emailAddress"]
            ).first()
            if user:
                if user.check_password(request.data["password"]):

                    return Response(
                        UserSerializer(user, many=False).data, status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {"Error": "You entered the wrong credentials"},
                        status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"Error": "User with the following Email does not exist"},
                    status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(data.errors, status.HTTP_400_BAD_REQUEST)
