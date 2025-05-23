from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False

        # return super().has_permission(request, view)
    
    # # this doesnt do a good job! has some flaws
    # def has_permission(self, request, view):      
    #     user = request.user
    #     print(user.get_all_permissions)

    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):  # appName.action_modelName|lowercased
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #     return False