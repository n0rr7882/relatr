from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserStaffOrOwner(BasePermission):
    def has_object_permission(self, request, view, object):
        return request.method in SAFE_METHODS or (
            request.user.is_staff or object.account.user == request.user)


class IsUserStaffOrThisObject(BasePermission):
    def has_object_permission(self, request, view, object):
        return request.method in SAFE_METHODS or (
            request.user.is_staff or object == request.user)
