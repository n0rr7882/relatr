from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'date_joined',
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followings = UserSerializer(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = (
            'user',
            'thumbnail',
            'created_at',
            'followings',
        )
