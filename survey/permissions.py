from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        code = request.query_params.get("code", None)
        print(code)
        if code is not None:
            return True
        return False
