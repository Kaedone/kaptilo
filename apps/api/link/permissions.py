from rest_framework.permissions import IsAuthenticated

__all__ = ["LinkPermission"]


class LinkPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
