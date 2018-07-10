from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.mixins import (
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from accounts.models import Account
from accounts.serializers import AccountSerializer

from .serializers import (
    ChainSerializer,
)
from .permissions import (
    IsUserStaffOrOwner,
    IsUserStaffOrThisObject
)
from .models import (
    Chain,
    ChainTag,
    ChainMention
)

import re


class CreateChainView(ListCreateAPIView):
    queryset = Chain.objects.select_related('account__user')
    queryset = queryset.prefetch_related('tags')
    queryset = queryset.prefetch_related('mentions__user')
    queryset = queryset.prefetch_related('likes__user').all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChainSerializer

    def post(self, request, format=None):
        serializer = ChainSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save(account=request.user.account)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DetailChainView(RetrieveUpdateDestroyAPIView):
    queryset = Chain.objects.select_related('account__user')
    queryset = queryset.prefetch_related('tags')
    queryset = queryset.prefetch_related('mentions__user')
    queryset = queryset.prefetch_related('likes__user').all()
    permission_classes = (IsUserStaffOrOwner,)
    serializer_class = ChainSerializer


class ParentChainView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        chain = self.get_object(pk)
        parent_chain = chain.parent_chain

        serializer = ChainSerializer(
            parent_chain,
            context={'request': request}
        )

        return Response(serializer.data)


class ChildChainView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        paginator = LimitOffsetPagination()

        chain = self.get_object(pk)
        child_chains = chain.get_child_chains()
        child_chains = child_chains.select_related('account__user')
        child_chains = child_chains.prefetch_related('tags')
        child_chains = child_chains.prefetch_related('mentions__user')
        child_chains = child_chains.prefetch_related('likes__user').all()

        results = paginator.paginate_queryset(child_chains, request)

        serializer = ChainSerializer(
            results,
            many=True,
            context={'request': request}
        )

        return paginator.get_paginated_response(serializer.data)


class ChainTagView(APIView):
    permission_classes = (IsUserStaffOrOwner,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk, tag_text, format=None):
        chain = self.get_object(pk)
        tag_pattern = re.compile(r'^[^\s`~!@#$%^&*()+=-]{2,}$')
        if not tag_pattern.match(tag_text):
            return Response({
                'tag_text': [
                    'This field must satisfy the condition of '
                    'the regex "^[^\s`~!@#$%^&*()+=-]{2,}$".'
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        if chain.add_tag(tag_text):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, tag_text, format=None):
        chain = self.get_object(pk)

        if chain.remove_tag(tag_text):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChainMentionView(APIView):
    permission_classes = (IsUserStaffOrOwner,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk, account_pk, format=None):
        chain = self.get_object(pk)
        target = get_object_or_404(Account, pk=account_pk)

        if chain.mention_to(target):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, account_pk, format=None):
        chain = self.get_object(pk)
        target = get_object_or_404(Account, pk=account_pk)

        if chain.cancel_mention_to(target):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChainLikeView(APIView):
    permission_classes = (IsUserStaffOrOwner,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk, account_pk, format=None):
        chain = self.get_object(pk)
        account = get_object_or_404(Account, pk=account_pk)

        if chain.liked_from(account):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, account_pk, foramt=None):
        chain = get_object_or_404(Chain, pk=pk)
        account = get_object_or_404(Account, pk=account_pk)

        if chain.unliked_from(account):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
