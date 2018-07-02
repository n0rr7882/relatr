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


class CreateTagView(APIView):
    permission_classes = (IsUserStaffOrOwner,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk, format=None):
        chain = self.get_object(pk)
        serializer = ChainTagSerializer(data=request.data)

        if serializer.is_valid():
            if chain.add_tag(serializer.data.get('tag')):
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request, pk, format=None):
        paginator = LimitOffsetPagination()

        chain = self.get_object(pk)
        tags = chain.get_tags()

        results = paginator.paginate_queryset(tags, request)
        serializer = ChainTagSerializer(results, many=True)

        return paginator.get_paginated_response(serializer.data)


class DetailTagView(APIView):
    permission_classes = (IsUserStaffOrOwner,)

    def get_object(self, pk):
        obj = get_object_or_404(Chain, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, tag, format=None):
        chain = self.get_object(pk)
        results = chain.tags.get(tag=tag)

        return Response({
            'chain': results.chain_id,
            'tag': results.tag
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk, tag, format=None):
        chain = self.get_object(pk)

        if chain.remove_tag(tag):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
