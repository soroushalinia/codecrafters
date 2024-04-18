from django.shortcuts import render

from core.models import CatalogModel
from core.serializers import CatalogSerializer

from rest_framework import permissions, viewsets

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = CatalogModel.objects.filter()
    serializer_class = CatalogSerializer
    permission_classes = []


def index(request):
    return render(request, 'core/index.html')

