from rest_framework import permissions


class IsUserIsaac(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
            if request.user.has_perm("products.product.view_product"):
                  return True
            return False






