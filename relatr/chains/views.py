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
    ChainTagSerializer,
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
    queryset = queryset.prefetch_related('mentions').all()
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
    queryset = queryset.prefetch_related('mentions').all()
    permission_classes = (IsUserStaffOrOwner,)
    serializer_class = ChainSerializer


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
