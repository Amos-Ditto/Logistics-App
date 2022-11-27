from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    Authorization = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["emailAddress", "fullName", "password", "Authorization"]
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
