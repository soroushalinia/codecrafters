from rest_framework import serializers
from core.models import CatalogModel

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModel
        fields = "__all__"