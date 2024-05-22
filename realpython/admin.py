from django.contrib import admin

from realpython.forms import DescribeTopicModelForm
from realpython.models import RealpythonTopicModel
from teacher.models import TeacherModel
from .models import RealpythonDescribeTopicModel

class DescribeRealPythonAdmin(admin.StackedInline):
    model = RealpythonDescribeTopicModel
    form = DescribeTopicModelForm


@admin.register(RealpythonTopicModel)
class TopicAdmin(admin.ModelAdmin):
    inlines = [DescribeRealPythonAdmin]
    
    def save_model(self, request, obj, form, change): 
        obj.author = TeacherModel.objects.get(author__id = request.user.id)
        obj.save()

    def get_queryset(self, request):
        if request.user.id == 1:
            qs = super().get_queryset(request)
            return qs 
        if request.user.is_superuser and not request.user.teachermodel.remove:
            qs = super().get_queryset(request)
            return qs.filter(author__author=request.user.teachermodel.author)  

    def has_add_permission(self, request):
        if request.user.id == 1:
            return True
        if request.user.is_superuser and not request.user.teachermodel.remove:
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