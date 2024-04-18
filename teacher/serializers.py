from rest_framework import serializers
from teacher.models import TeacherModel

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['author', 'name', 'title', 'image', 'remove', 'describe', 'search', 'linkedin_username', 'email', 'github_username', 'telegram_username']