from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """ 

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if not obj.stream:
            return False
        obj = obj.stream
        if not request.user.is_anonymous() and request.method in permissions.SAFE_METHODS:
            members = obj.members.filter(user=request.user)
            if len(members):
                return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
