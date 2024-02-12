from django.contrib import admin
from django.http import HttpRequest
from .models import ConnectModel
# Register your models here.


@admin.register(ConnectModel)
class ConnectAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        if request.user.id == 1:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.id == 1:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
         return False