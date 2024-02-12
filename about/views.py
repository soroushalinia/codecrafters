from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import ConnectForm
from django.contrib import messages

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about/about.html'

class ConnectView(FormView):
    form_class = ConnectForm
    template_name = 'about/form.html'
    success_url = '/about'

    def get_success_url(self):
        messages.success(self.request, 'درخواست شما با موفقیت ثبت شد')
        return self.success_url
