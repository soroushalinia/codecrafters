from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import NewsModel
from .forms import NewsCommentForm
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse


class NewsListView(ListView):
    queryset = NewsModel.objects.filter(public=True)
    template_name = 'news/list.html'
    ordering = ('created')


class NewsCommentView(FormMixin, DetailView):
    template_name='news/post.html'
    queryset = NewsModel.objects.filter(public=True)
    form_class = NewsCommentForm

    def get_success_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(NewsCommentView, self).get_context_data(**kwargs)
        context['form'] = NewsCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.news = self.object
            obj.save()
            messages.success(self.request, 'کامنت شما با موفقیت ثبت شد')
            return super(NewsCommentView, self).form_valid(form)
        else:
            messages.error(self.request, 'لطفا تمامی فیلدها را پر کنید')
            return super(NewsCommentView, self).form_invalid(form)
