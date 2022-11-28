from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import DeliveryManager, DeliveryStation
from .serializers import (
    UserSerializer,
    UserLoginSerializer,
    DeliveryManagerSerializer,
    DeliveryStationSerializer,
)
from .schemas import get_managers_response_schema, post_managers_response_schema

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


class DeliveryManagerView(APIView):

    emailAddress = openapi.Parameter(
        "emailAddress",
        openapi.IN_QUERY,
        description="Get delivery manager by Email Address",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Get Delivery Managers by emails or All but paginated dicts",
        manual_parameters=[emailAddress],
        responses=get_managers_response_schema,
    )
    def get(self, request, format=None):
        params = request.query_params

        if "emailAddress" in params:

            obj = DeliveryManager.objects.filter(
                user__emailAddress=params["emailAddress"]
            ).first()
            if obj:
                return Response(DeliveryManagerSerializer(obj).data, status.HTTP_200_OK)
            else:
                return Response(
                    {"Error": "Manager with this email Address doesn't exists"},
                    status.HTTP_401_UNAUTHORIZED,
                )
        else:
            obj = DeliveryManager.objects.all()

            return Response(
                DeliveryManagerSerializer(obj, many=True).data, status.HTTP_200_OK
            )

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Authenticates an existing user based on their email and their password. If successful, an access token and a refresh token will be returned.",
        request_body=DeliveryManagerSerializer,
        responses=post_managers_response_schema,
    )
    def post(self, request, format=None):
        data = DeliveryManagerSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.filter(emailAddress=request.data["user"]).first()
            if user:
                manager = data.create(request.data)

                if manager:
                    return Response(
                        DeliveryManagerSerializer(manager).data,
                        status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"Error": "Found station id doesn't exist yet"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
            else:
                return Response(
                    {"Error": "User with this email doesn't exist yet"},
                    status.HTTP_401_UNAUTHORIZED,
                )

        else:
            return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeliveryStationView(APIView):
    placeName = openapi.Parameter(
        "placeName",
        openapi.IN_QUERY,
        description="Get stations by placeName",
        type=openapi.TYPE_STRING,
    )
    region = openapi.Parameter(
        "region",
        openapi.IN_QUERY,
        description="Get stations by region",
        type=openapi.TYPE_STRING,
    )
    town = openapi.Parameter(
        "town",
        openapi.IN_QUERY,
        description="Get stations by town",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        tags=["Address"],
        operation_description="List Delivery Stations & Addresses and also can searchable with parameters `placeName` or `region` or `town`",
        manual_parameters=[placeName, region, town],
        responses={200: DeliveryStationSerializer(many=True)},
    )
    def get(self, request):
        params = request.query_params

        if "placeName" in params:
            station = DeliveryStation.objects.filter(
                placeName__icontains=params["placeName"]
            )
            return Response(
                DeliveryStationSerializer(station, many=True).data, status.HTTP_200_OK
            )
        if "region" in params:
            station = DeliveryStation.objects.filter(region__icontains=params["region"])
            return Response(
                DeliveryStationSerializer(station, many=True).data, status.HTTP_200_OK
            )
        if "town" in params:
            station = DeliveryStation.objects.filter(region__icontains=params["town"])
            return Response(
                DeliveryStationSerializer(station, many=True).data, status.HTTP_200_OK
            )

        station = DeliveryStation.objects.all()
        return Response(
            DeliveryStationSerializer(station, many=True).data, status.HTTP_200_OK
        )
