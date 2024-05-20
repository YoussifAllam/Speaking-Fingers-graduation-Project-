from rest_framework import permissions

class IsAdminOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all users (including non-authenticated) to perform POST
        if request.method == 'POST':
            return True

        # Allow only admin users to perform other CRUD operations
        return request.user 