from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import TeacherModel
# Create your views here.


class TeacherListView(ListView):
    queryset = TeacherModel.objects.filter(remove=False)
    template_name = 'teacher/list.html'


class TeacherDetailView(DetailView):
    queryset = TeacherModel.objects.filter(remove=False)
    template_name = 'teacher/detail.html'