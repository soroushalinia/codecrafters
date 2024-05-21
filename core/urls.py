from django.urls import path
# from .views import index
from .views import CatalogViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"", CatalogViewSet)

app_name = 'core'

urlpatterns = router.urls

# urlpatterns = [
#     path('', index, name='index'),
# ]