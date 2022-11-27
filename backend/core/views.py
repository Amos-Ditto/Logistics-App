from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserLoginSerializer

User = get_user_model()


class UserView(APIView):
    def post(self, request):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            user = data.create(request.data)

            return Response(UserSerializer(user).data, status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
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
