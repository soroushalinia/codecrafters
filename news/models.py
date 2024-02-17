from django.db import models
from teacher.models import TeacherModel
from ckeditor.fields import RichTextField
from core.models import CatalogModel
# Create your models here.

class NewsModel(models.Model):
    author = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    catalog = models.ForeignKey(CatalogModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته بندی')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to="news", verbose_name='تضویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    public = models.BooleanField(default=False, verbose_name='انتشار')
    describe = RichTextField(verbose_name='توضیحات')
    search = models.TextField(verbose_name='توضیح کوتاه')

    def __str__(self) -> str:
        return f'{self.title}'
        
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ['created']


class NewsCommentModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='خبر')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='پاسخ به خبر')
    name = models.CharField(max_length=100, verbose_name='نام')
    describe = models.TextField(verbose_name='توضیحات')
    public = models.BooleanField(default=False, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:        
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
        ordering = ['created']