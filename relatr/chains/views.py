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
    CreateChainSerializer,
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
