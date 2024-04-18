from django.contrib.auth.models import Group, User
from rest_framework import serializers

from blog.models import BlogModel, CommentBlogtModel

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['slug', 'author',  'catalog', 'title', 'image', 'created', 'public', 'describe', 'search' ]


class CommentBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentBlogtModel
        fields = ['blog', 'parent', 'name', 'describe', 'public', 'created']