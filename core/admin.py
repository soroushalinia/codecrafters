from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CatalogModel



@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser and not request.user.teachermodel.remove:
            qs = super().get_queryset(request)
            return qs
        
    def has_add_permission(self, request):
        if request.user.is_superuser and not request.user.teachermodel.remove:
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser and not request.user.teachermodel.remove:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
         return False



class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        if request.user.id == 1:
            qs = super().get_queryset(request)
            return qs 
        if request.user.is_superuser and not request.user.teachermodel.remove:
            qs = super().get_queryset(request)
            return qs.filter(id=request.user.id)
        
    def has_add_permission(self, request):
        if request.user.id == 1:
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.id == 1:
            return True
        if request.user.is_superuser and not request.user.teachermodel.remove:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
         return False
    
class CustomGroupAdmin(GroupAdmin):
    def has_add_permission(self, request):
        if request.user.id == 1:
            return True 
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.id == 1:
                    return True 
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

# Unregister the original User and Group admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Register the custom User and Group admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)