from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission



class MostlyUsedPermissions(BasePermission):
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]


