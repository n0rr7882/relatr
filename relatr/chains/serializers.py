from rest_framework import serializers
from .models import (
    Chain,
    ChainTag,
    ChainMention,
)
from accounts.models import (
    Account,
    Follow,
)
from accounts.serializers import (
    UserSerializer,
    AccountSerializer,
)


class CreateChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = (
            'account',
            'text',
            'image',
        )


class ChainSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tag',
    )
    mentions = AccountSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Chain
        fields = (
            'account',
            'text',
            'image',
            'tags',
            'mentions',
        )
        extra_kwargs = {
            'account': {'write_only': True}
        }
