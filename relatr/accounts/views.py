from rest_framework import (
    views,
    viewsets,
    permissions,
    pagination,
    status,
    response
)
from . import serializers


class UserView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = serializers.UserSerializer


class UpdatePasswordView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = serializers.ChangePasswordSerializer(data=request.data)

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
