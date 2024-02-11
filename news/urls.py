from django.urls import path
from .views import NewsListView, NewsCommentView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<pk>/', NewsCommentView.as_view(), name='news_detail'),
]