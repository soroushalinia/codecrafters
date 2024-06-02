from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView

from blog.serializers import BlogSerializer
from .models import BlogModel
from .forms import BlogCommentForm
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse

from rest_framework import permissions, viewsets

class BlogListView(ListView):
    queryset = BlogModel.objects.filter(public=True)
    template_name = 'blog/list.html'
    ordering = ('-created')

class BlogCommentView(DetailView):
    queryset = BlogModel.objects.filter(public=True)
    template_name='blog/post.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any):
        context = super(BlogCommentView, self).get_context_data(**kwargs)
        context['object_list'] = BlogModel.objects.filter(catalog = context['object'].catalog, public=True).order_by('-created') 
        print(context)
        return context
    

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.filter(public=True)
    serializer_class = BlogSerializer
    lookup_field = "slug"

