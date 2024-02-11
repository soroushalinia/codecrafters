from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CatalogModel



@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False 
    

class CustomUserAdmin(UserAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
class CustomGroupAdmin(GroupAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True 
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

# Unregister the original User and Group admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Register the custom User and Group admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)