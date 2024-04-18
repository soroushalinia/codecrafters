from django.shortcuts import render
from django.views.generic import DetailView, ListView

from teacher.serializers import TeacherSerializer
from .models import TeacherModel
from topic.models import TopicModel
# Create your views here.
from rest_framework import permissions, viewsets


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.filter(remove=False)
    serializer_class = TeacherSerializer
    permission_classes = []


class TeacherListView(ListView):
    queryset = TeacherModel.objects.filter(remove=False)
    template_name = 'teacher/list.html'


class TeacherDetailView(DetailView):
    queryset = TeacherModel.objects.filter(remove=False)
    template_name = 'teacher/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        context['topics'] = TopicModel.objects.filter(author__id = context['object'].id) 
        return context