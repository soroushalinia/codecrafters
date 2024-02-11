from django.contrib import admin
from .models import TeacherModel
# Register your models here.


@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False