from rest_framework import (
    serializers,
    exceptions,
)

from django.contrib.auth.password_validation import validate_password
from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'hidden'},
        write_only=True,
        required=False,
    )
    thumbnail = serializers.ImageField(
        source='account.thumbnail',
        read_only=True
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = models.User
        fields = (
            'id',
            'thumbnail',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'followers',
        )

    def validate(self, data):
        user = models.User(**data)
        errors = dict()

        if 'password' in data:
            try:
                validate_password(password=data['password'], user=models.User)

            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data.pop('password')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Account
        fields = (
            'id',
            'user',
            'thumbnail',
            'created_at',
            'followings',
        )
