from rest_framework import serializers
from topic.models import TopicModel, DescribeTopicModel, CommentTopicModel
class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicModel
        fields = ["slug", "author", "catalog", "name", "title", "image", "the_end", "created", "search"]


class DescribeTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DescribeTopicModel
        fields = ["slug", "topic", "number", "title", "public", "describtion", "created", "search"]


class CommentTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentTopicModel
        fields = ["describetapic", "parent", "name", "describe", "public", "created"]