from django.urls import path
from .views import BlogListView, BlogCommentView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<pk>/', BlogCommentView.as_view(), name='blog_detail'),
]