from django.contrib.auth.models import Group, User
from rest_framework import serializers

from blog.models import BlogModel, CommentBlogtModel
from core.serializers import CatalogSerializer
from teacher.serializers import TeacherSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = TeacherSerializer()
    catalog = CatalogSerializer()
    
    class Meta:
        model = BlogModel
        fields = "__all__"
        

class CommentBlogSerializer(serializers.ModelSerializer):

    blog = BlogSerializer()
    class Meta:
        model = CommentBlogtModel
        fields = "__all__"
    