from typing import Any
from .forms import TopicCommentForm
from django.views.generic import DetailView, ListView
from .models import TopicModel, DescribeTopicModel, CommentTopicModel
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse
# Create your views here.


class TopicListViews(ListView):
    model = TopicModel
    template_name = 'topic/list.html'


class TopicDetailView(DetailView):
    model = TopicModel
    template_name = 'topic/detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['object_list'] = DescribeTopicModel.objects.filter(topic__id = self.kwargs['pk'], public=True).order_by('number') 
        return context


class TopicDescribeCommentView(DetailView):
    queryset = DescribeTopicModel.objects.filter(public=True)
    template_name='topic/post.html'

    def get_context_data(self, **kwargs: Any):
        context = super(TopicDescribeCommentView, self).get_context_data(**kwargs)
        context['object_list'] = DescribeTopicModel.objects.filter(topic = context['object'].topic, public=True).order_by('number') 
        context['topics'] = TopicModel.objects.filter(catalog = context['object'].topic.catalog)
        print(context)
        return context

'''
class TopicDescribeCommentView(FormMixin, DetailView):
    queryset = DescribeTopicModel.objects.filter(public=True)
    template_name='topic/post.html'
    form_class = TopicCommentForm
    
    def get_success_url(self):
        return reverse('topic:topic_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(TopicDescribeCommentView, self).get_context_data(**kwargs)
        context['object_list'] = DescribeTopicModel.objects.filter(topic__id = self.kwargs['pk'], pulic=True).exclude(id=self.kwargs['pk']).order_by('number') 
        context['form'] = TopicCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.describetapic = self.object
            obj.save()
            messages.success(self.request, 'کامنت شما با موفقیت ثبت شد')
            return super(TopicDescribeCommentView, self).form_valid(form)
        else:
            messages.error(self.request, 'لطفا تمامی فیلدها را پر کنید')
            return super(TopicDescribeCommentView, self).form_invalid(form)
'''