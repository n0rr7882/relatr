from rest_framework.permissions import BasePermission


class IsUserStaffOrOwner(BasePermission):
    def has_object_permission(self, request, view, object):
        return request.method == 'GET' or (
            request.user.is_staff or object.account.user == request.user)


class IsUserStaffOrThisObject(BasePermission):
    def has_object_permission(self, request, view, object):
        return request.method == 'GET' or (
            request.user.is_staff or object == request.user)
