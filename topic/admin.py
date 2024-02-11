from django.contrib import admin
from .models import TopicModel, DescribeTopicModel, CommentTopicModel
# Register your models here.


@admin.register(TopicModel)
class TapicAdmin(admin.ModelAdmin):
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    

@admin.register(DescribeTopicModel)
class DescribeTaoicAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(CommentTopicModel)
class CommentTopicAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False