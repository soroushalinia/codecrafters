from django.urls import path
from .views import TopicListViews, TopicDetailView, TopicDescribeCommentView

app_name = 'topic'

urlpatterns = [
    path('', TopicListViews.as_view(), name='topics'),
    path('<pk>/', TopicDetailView.as_view(), name='topic'),
    path('describe/<pk>/', TopicDescribeCommentView.as_view(), name='describe'),
]