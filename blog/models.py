from django.db import models
from teacher.models import TeacherModel
from core.models import CatalogModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import re

# Create your models here.

class BlogModel(models.Model):
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    catalog = models.ForeignKey(CatalogModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته بندی')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to="blog", verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    public = models.BooleanField(default=False, verbose_name='انتشار')
    describe = RichTextField(verbose_name='توضیحات')
    search = models.TextField(verbose_name='توضیح کوتاه')
    
    def __str__(self) -> str:
        return f'{self.title}'

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        base_slug =  re.sub(r'[@#\\|/*&%$^+=!.,{}()_?]', '-', self.title)
        if not self.id:
            try:
                latest_object = BlogModel.objects.latest('id')
                latest_id = latest_object.id
                number = latest_id + 1
            except:
                number = 1
        else:
            number = self.id
        self.slug = f"{number}-{base_slug}".replace(' ', '-')
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = " وبلاگ ها"
        ordering = ['created']


class CommentBlogtModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='وبلاگ')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='پاسخ به کامنت')
    name = models.CharField(max_length=100, verbose_name='نام')
    describe = models.TextField(verbose_name='توضیحات')
    public = models.BooleanField(default=False, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:        
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
        ordering = ['created']

