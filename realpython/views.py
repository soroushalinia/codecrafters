from .serializers import RealPythonDescribeCommentSerializer, RealPythonSerializer
from .models import RealpythonTopicModel, RealpythonDescribeTopicModel
from rest_framework import viewsets

class RealPythonViewSet(viewsets.ModelViewSet):
    queryset = RealpythonTopicModel.objects.all()
    serializer_class = RealPythonSerializer
    lookup_field = "slug"


class RealPythonDescribeCommentViewSet(viewsets.ModelViewSet):
    queryset = RealpythonDescribeTopicModel.objects.filter(public=True)
    serializer_class = RealPythonDescribeCommentSerializer
    lookup_field = "slug"

