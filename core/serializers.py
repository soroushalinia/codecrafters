from rest_framework import serializers
from core.models import CatalogModel

class CatalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogModel
        fields = ["title"]