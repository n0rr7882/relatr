from rest_framework import serializers
from .models import (
    Chain,
    Hashtag,
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


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = (
            'id',
            'name',
        )


class ChainSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    tags = HashtagSerializer(
        many=True,
        read_only=True
    )
    mentions = AccountSerializer(
        many=True,
        read_only=True,
    )
    likes = AccountSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Chain
        fields = (
            'id',
            'account',
            'text',
            'image',
            'tags',
            'mentions',
            'likes',
            'parent_chain',
            'child_chains',
            'created_at',
        )
        read_only_fields = (
            'child_chains',
        )
        extra_kwargs = {
            'account': {'write_only': True}
        }
