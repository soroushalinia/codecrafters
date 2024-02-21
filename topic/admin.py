from django.contrib import admin
from .models import TopicModel, DescribeTopicModel
from .forms import DescribeTopicModelForm
from teacher.models import TeacherModel
# Register your models here.

class DescribeTaoicAdmin(admin.StackedInline):
    model = DescribeTopicModel
    form = DescribeTopicModelForm

    fieldsets = [
        ('', {'fields': ['topic', 'number', 'title', 'public', 'search',]}),
        ('', {'fields': ['describtion'], 'classes': ['full-row']}),
    ]

@admin.register(TopicModel)
class TopicAdmin(admin.ModelAdmin):
    inlines = [DescribeTaoicAdmin]
    exclude = ['author', ]
    
    def save_model(self, request, obj, form, change):
        # Set the user field when creating a new object
        if not obj.author:
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

    
'''
@admin.register(CommentTopicModel)
class CommentTopicAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        if request.user.id == 1:
            qs = super().get_queryset(request)
            return qs 
        if request.user.is_superuser and not request.user.teachermodel.remove:
            qs = super().get_queryset(request)
            return qs
        
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
        return 
'''