from rest_framework import serializers

from core.serializers import CatalogSerializer
from teacher.serializers import TeacherSerializer
# from .models import DescribeTopicModel, TopicModel
from .models import RealpythonDescribeTopicModel, RealpythonTopicModel

class RealPythonDescribeCommentSerializer(serializers.ModelSerializer):
    # topic = RealPythonSerializer()

    class Meta:
        model = RealpythonDescribeTopicModel
        fields = "__all__"

class RealPythonSerializer(serializers.ModelSerializer):
    author = TeacherSerializer()
    catalog = CatalogSerializer()
    describe = RealPythonDescribeCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = RealpythonTopicModel
        fields = "__all__"

