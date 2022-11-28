from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .models import DeliveryManager, DeliveryStation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    Authorization = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["emailAddress", "fullName", "Authorization", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            emailAddress=validated_data["emailAddress"],
            fullName=validated_data["fullName"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

    def get_Authorization(self, user):
        return getUserToken(user)


# User JWT header token
def getUserToken(user):
    token, _ = Token.objects.get_or_create(user=user)
    return "Token " + token.key


class UserLoginSerializer(serializers.Serializer):
    emailAddress = serializers.EmailField()
    password = serializers.CharField(min_length=6)


class DeliveryManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryManager
        fields = ["id", "user", "station", "active"]
        depth = 1

    def create(self, validated_data):
        station = DeliveryStation.objects.filter(id=validated_data["station"]).first()
        if station:
            manager, _ = DeliveryManager.objects.get_or_create(
                user_id=validated_data["user"],
                station=station,
            )

            return manager


class DeliveryStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStation
        fields = [
            "id",
            "placeName",
            "region",
            "town",
            "description",
            "longitude",
            "latitude",
            "active",
        ]
