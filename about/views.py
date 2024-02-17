from django.views.generic import TemplateView
from .forms import ConnectForm
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse
# Create your views here.


class AboutView(FormMixin, TemplateView):
    template_name='about/about.html'
    form_class = ConnectForm
    
    def get_success_url(self):
        return reverse('about:about')

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['form'] = ConnectForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = self.object
            obj.save()
            messages.success(self.request, 'کامنت شما با موفقیت ثبت شد')
            return super(AboutView, self).form_valid(form)
        else:
            messages.error(self.request, 'لطفا تمامی فیلدها را پر کنید')
            return super(AboutView, self).form_invalid(form)
