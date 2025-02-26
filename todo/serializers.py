from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")  # Makes 'user' read-only

    class Meta:
        model = ToDo
        fields = ["id", "title", "completed", "created_at", "user"]


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims (optional)
        token["username"] = user.username
        return token
