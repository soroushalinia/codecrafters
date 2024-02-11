from django.contrib import admin
from .models import NewsModel, NewsCommentModel
# Register your models here.


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False