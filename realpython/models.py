from django.db import models
from teacher.models import TeacherModel 
from ckeditor.fields import RichTextField
from core.models import CatalogModel
from django.utils.text import slugify
import re


class RealpythonTopicModel(models.Model):
    slug = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نام مدرس')
    catalog = models.ForeignKey(CatalogModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته بندی')
    name = models.CharField(max_length=250, verbose_name='نام')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    image = models.ImageField(upload_to='topics', verbose_name='تصویر')
    the_end = models.BooleanField(default=False, verbose_name='پایان')
    created = models.DateTimeField(verbose_name='تاریخ')
    search = models.TextField(verbose_name='متن جستجو')
    
    def delete(self, *args, **kwargs):
        pass
    

    def save(self, *args, **kwargs):
        base_slug =  re.sub(r'[@#\\|/*&%$^+=!.,{}()_?]', '-', self.title)
        if not self.id:
            try:
                latest_object = RealpythonTopicModel.objects.latest('id')
                latest_id = latest_object.id
                number = latest_id + 1
            except:
                number = 1
        else:
            number = self.id
        self.slug = f"{number}-{base_slug}".replace(' ', '-')
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = "موضوع"
        verbose_name_plural = "موضوعات"
        ordering = ['created']



class RealpythonDescribeTopicModel(models.Model):
    slug = models.CharField(max_length=255, null=True, blank=True)
    topic = models.ForeignKey(RealpythonTopicModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='موضوع')
    number = models.PositiveBigIntegerField(verbose_name='شماره')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    public = models.BooleanField(default=False, verbose_name='انتشار')
    describtion = RichTextField(blank=True, null=True, verbose_name='توضیحات')
    created = models.DateTimeField(verbose_name='تاریخ')
    search = models.TextField(verbose_name='متن جستجو')
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        base_slug =  re.sub(r'[@#\\|/*&%$^+=!.,{}()_?]', '-', self.title)
        if not self.id:
            try:
                latest_object = RealpythonTopicModel.objects.latest('id')
                latest_id = latest_object.id
                number = latest_id + 1
            except:
                number = 1
        else:
            number = self.id
        self.slug = f"{number}-{base_slug}".replace(' ', '-')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "جلسه"
        verbose_name_plural = "جلسات"
        ordering = ['created']

class RealPythonCommentTopicModel(models.Model):
    describetopic = models.ForeignKey(RealpythonDescribeTopicModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='تاپیک')
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
