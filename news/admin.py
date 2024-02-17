from django.contrib import admin
from .models import NewsModel, NewsCommentModel
from teacher.models import TeacherModel
# Register your models here.


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
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
            return qs.filter(id=request.user.id)
        
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
    