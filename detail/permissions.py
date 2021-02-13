from rest_framework import permissions
 
class IsOwner(permissions.BasePermission):
    my_safe_method=['GET','PUT','POST']
    
    def has_permission(self, request,view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj==request.user
     

