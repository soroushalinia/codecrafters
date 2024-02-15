from django.urls import path
from .views import TeacherListView, TeacherDetailView

app_name = 'teacher'

urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers'),
    path('detail', TeacherDetailView.as_view(), name='teacher'),
]