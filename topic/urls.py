from django.urls import path
from .views import TopicDescribeCommentViewSet, TopicViewSet

app_name = 'topic'


urlpatterns = [
    # path('', TopicListViews.as_view(), name='topics'),
    # path('<slug>/', TopicDetailView.as_view(), name='topic'),
    # path('session/<slug>/', TopicDescribeCommentView.as_view(), name='session'),
    path('', TopicViewSet.as_view({'get': 'list'})),
    path('session/<slug>/', TopicDescribeCommentViewSet.as_view({'get': 'retrieve'})),
    path('<slug>', TopicViewSet.as_view({'get': 'retrieve'})),
    # path('session/', TopicDescribeCommentViewSet.as_view({'get': 'list'})),
]