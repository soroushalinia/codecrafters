from django.db import models
# Create your models here.


class CatalogModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.title}'
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['title']