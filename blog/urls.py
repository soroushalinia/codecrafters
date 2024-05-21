from django.urls import path
# from .views import BlogListView, BlogCommentView
from .views import BlogViewSet
from rest_framework import routers

app_name = 'blog'

# urlpatterns = [
#     path('', BlogListView.as_view(), name='blogs'),
#     path('<slug>/', BlogCommentView.as_view(), name='blog'),
# ]

router = routers.SimpleRouter()

router.register(r'', BlogViewSet)

urlpatterns = router.urls