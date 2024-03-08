from django.urls import path
from .views import TopicListViews, TopicDetailView, TopicDescribeCommentView

app_name = 'topic'

urlpatterns = [
    path('', TopicListViews.as_view(), name='topics'),
    path('<slug>/', TopicDetailView.as_view(), name='topic'),
    path('session/<slug>/', TopicDescribeCommentView.as_view(), name='session'),
]