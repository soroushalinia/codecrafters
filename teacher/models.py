from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class TeacherModel(models.Model):
    author = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='نام')
    title = models.CharField(max_length=500, verbose_name='عتوان')
    image = models.ImageField(upload_to='teacher', null=True, blank=True, verbose_name='تصویر')
    remove = models.BooleanField(default=False, verbose_name='حذف')
    describe = RichTextField(verbose_name='توضیحات')
    search = models.TextField(verbose_name='متن جستجو از خود')
    linkedin_username = models.CharField(max_length=255, null=True, blank=True, verbose_name='یوزرنیم لینکدین')
    email = models.EmailField(max_length=255, verbose_name='ایمیل')
    github_username = models.CharField(max_length=255, verbose_name='یوزرنیم گیت‌هاب')
    telegram_username = models.CharField(max_length=255, null=True, blank=True, verbose_name=' یوزرنیم تلگرام')

    def __str__(self) -> str:
        return f'{self.name}'

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "معلم"
        verbose_name_plural = "معلم ها"
        ordering = ['name']
