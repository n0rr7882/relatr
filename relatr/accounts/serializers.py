from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'account',
        )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followings = UserSerializer(many=True)

    class Meta:
        model = models.Account
        fields = (
            'user',
            'thumbnail',
            'created_at',
            'followings',
        )
