from django.urls import path
from .views import ConnectView, AboutView

app_name = 'about'

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('form/', ConnectView.as_view(), name='form'),
]