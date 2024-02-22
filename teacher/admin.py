from django.contrib import admin
from .models import TeacherModel
# Register your models here.
from django.contrib.auth.models import User
from django.http import Http404

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.id == 1:
            qs = super().get_queryset(request)
            return qs 
        if request.user.is_superuser and not request.user.teachermodel.remove:
            qs = super().get_queryset(request)
            return qs.filter(author__id=request.user.id)
        
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
    
