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

# Create your views here.

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
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    queryset = BlogModel.objects.filter(public=True)
    serializer_class = BlogSerializer
    permission_classes = []

'''
class BlogCommentView(FormMixin, DetailView):
    queryset = BlogModel.objects.filter(public=True)
    template_name='blog/post.html'
    form_class = BlogCommentForm
    
    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BlogCommentView, self).get_context_data(**kwargs)
        context['form'] = BlogCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = self.object
            obj.save()
            messages.success(self.request, 'کامنت شما با موفقیت ثبت شد')
            return super(BlogCommentView, self).form_valid(form)
        else:
            messages.error(self.request, 'لطفا تمامی فیلدها را پر کنید')
            return super(BlogCommentView, self).form_invalid(form)
'''