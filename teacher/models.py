from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class TeacherModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام')
    title = models.CharField(max_length=500, verbose_name='عتوان')
    image = models.ImageField(upload_to='teacher', null=True, blank=True, verbose_name='تصویر')
    delete = models.BooleanField(default=False, verbose_name='حذف')
    describe = RichTextField(verbose_name='توضیحات')
    search = models.TextField(verbose_name='متن جستجو')
    linkdin = models.URLField(null=True, blank=True, verbose_name='لینکدین')
    email = models.EmailField(verbose_name='ایمیل')
    telegram = models.URLField(null=True, blank=True, verbose_name='تلگرام')

    def __str__(self) -> str:
        return f'{self.name}'
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.translate.delete()
        super(TeacherModel, self).delete()

    class Meta:
        verbose_name = "معلم"
        verbose_name_plural = "معلم ها"
        ordering = ['name']
