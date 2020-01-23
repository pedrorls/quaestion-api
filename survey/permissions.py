from rest_framework import permissions
from user.models import User

class IsUserCodeSupplied(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        code = request.query_params.get("code", None)
        try:
            user = User.objects.get(key=code)
            return True
        except:
            return False

        
