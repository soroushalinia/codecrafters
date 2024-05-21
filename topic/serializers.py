from rest_framework import serializers

from core.serializers import CatalogSerializer
from teacher.serializers import TeacherSerializer
from .models import DescribeTopicModel, TopicModel


class TopicSerializer(serializers.ModelSerializer):
    author = TeacherSerializer()
    catalog = CatalogSerializer()
    
    class Meta:
        model = TopicModel
        fields = "__all__"

class TopicDescriveCommentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = DescribeTopicModel
        fields = "__all__"