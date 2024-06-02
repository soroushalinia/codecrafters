from django.urls import path
from .views import RealPythonViewSet, RealPythonDescribeCommentViewSet

app_name = 'realpython'

urlpatterns = [
    path('', RealPythonViewSet.as_view({'get': 'list'})),
    path('session/<slug>/', RealPythonDescribeCommentViewSet.as_view({'get': 'retrieve'})),
    path('<slug>', RealPythonViewSet.as_view({'get': 'retrieve'})),
   
]