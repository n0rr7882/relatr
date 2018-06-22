from rest_framework import permissions


class IsUserStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        return request.user.is_staff or object.user == request.user
