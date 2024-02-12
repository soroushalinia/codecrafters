from django.db import models

# Create your models here.

class ConnectModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    describe = models.TextField(verbose_name='توضیحات')
    created = models.TimeField(auto_now_add=True, verbose_name='تاریخ')
    read = models.BooleanField(default=False, verbose_name='خوانده شده')

    def __str__(self) -> str:
        return f'{self.title}'
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = 'ارتیاط با ما'
        verbose_name_plural = 'ارتیاط با ما'
        ordering = ['created', 'read']
