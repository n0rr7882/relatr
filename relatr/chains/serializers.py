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


class ChainTagSerializer(serializers.ModelSerializer):
    tag = serializers.RegexField(
        r'^[^\s`~!@#$%^&*()+=-]{2,}$',
        required=True
    )

    class Meta:
        model = ChainTag
        fields = (
            'chain',
            'tag',
        )
        read_only_fields = (
            'chain',
        )


class ChainSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    tags = ChainTagSerializer(
        many=True,
        read_only=True,
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
