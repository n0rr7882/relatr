from rest_framework import (
    views,
    viewsets,
    permissions,
    pagination,
    status,
    response,
    exceptions,
)
from django import shortcuts
from . import serializers as account_serializers
from . import permissions as account_permissions
from . import models as account_models


class UserView(viewsets.ModelViewSet):
    queryset = account_models.User.objects.all().prefetch_related('account__followings')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = account_serializers.UserSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = account_models.Account.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = account_serializers.AccountSerializer


class UpdatePasswordView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        return shortcuts.get_object_or_404(User, pk)

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = account_serializers.ChangePasswordSerializer(
            data=request.data
        )

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")

            if not self.object.check_password(old_password):
                return response.Response(
                    {
                        "old_password": [
                            "Wrong password."
                        ]
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        return response.Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
