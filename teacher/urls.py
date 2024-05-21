from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherViewSet
from rest_framework import routers

app_name = 'teacher'

router = routers.SimpleRouter()

router.register(r'', TeacherViewSet)

# urlpatterns = [
    # path('', TeacherListView.as_view(), name='teachers'),
    # path('<pk>', TeacherDetailView.as_view(), name='teacher'),
# ] 

urlpatterns = router.urls