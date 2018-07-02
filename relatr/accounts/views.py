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
    AccountSerializer,
    ChangePasswordSerializer,
    UserSerializer,
)
from .permissions import (
    IsUserStaffOrOwner,
    IsUserStaffOrThisObject
)
from .models import (
    User,
    Account,
    Follow,
)


class CreateUserView(ListCreateAPIView):
    queryset = User.objects.prefetch_related('account').all()
    serializer_class = UserSerializer


class DetailUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.select_related('account').all()
    permission_classes = (IsUserStaffOrThisObject,)
    serializer_class = UserSerializer


class ListAccountView(ListAPIView):
    queryset = Account.objects.select_related('user').all()
    serializer_class = AccountSerializer


class DetailAccountView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.select_related('user').all()
    permission_classes = (IsUserStaffOrOwner,)
    serializer_class = AccountSerializer


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None):
        self.object = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")

            if not self.object.check_password(old_password):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FollowView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return get_object_or_404(Account, pk=pk)

    def post(self, request, pk, format=None):
        if request.user.account.follow_to(self.get_object(pk)):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, format=None):
        if request.user.account.unfollow_to(self.get_object(pk)):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AccountFollowingsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        paginator = LimitOffsetPagination()

        account = get_object_or_404(Account, pk=pk)
        followers = account.get_followings()

        results = paginator.paginate_queryset(followers, request)

        serializer = AccountSerializer(
            results,
            many=True,
            context={'request': request}
        )

        return paginator.get_paginated_response(serializer.data)


class AccountFollowersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        context = {'request': request}
        paginator = LimitOffsetPagination()

        account = get_object_or_404(Account, pk=pk)
        followers = account.get_followers()

        results = paginator.paginate_queryset(followers, request)

        serializer = AccountSerializer(
            results,
            many=True,
            context={'request': request}
        )

        return paginator.get_paginated_response(serializer.data)
