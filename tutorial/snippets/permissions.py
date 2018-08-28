from rest_framework import permissions


# region Owner Or Read Only Permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission permits only the owner to edit the object.
    """

    def has_object_permission(self, request, view, obj):
        """Tests object's owner permission"""

        # Read permissions are allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to an owner.
        return obj.owner == request.user

# endregion
