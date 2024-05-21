from rest_framework import serializers
from teacher.models import TeacherModel

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"