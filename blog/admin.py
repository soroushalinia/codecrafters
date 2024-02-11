from django.contrib import admin
from .models import BlogModel, CommentBlogtModel

# Register your models here.


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    

@admin.register(CommentBlogtModel)
class CommentBlogAdmin(admin.ModelAdmin):

        def has_delete_permission(self, request, obj=None):
            if request.user.is_superuser:
                return True
            return False

        def has_add_permission(self, request, obj=None):
            if request.user.is_superuser:
                return True
            return False