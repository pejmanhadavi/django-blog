from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, verbose_name='نام دسته')
    slug = models.SlugField(blank=False, null=False, allow_unicode=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50, verbose_name='عنوان')
    slug = models.SlugField(blank=False, null=False)
    category = models.ForeignKey(related_name='category', on_delete=models.CASCADE, to=Category)
    thumbnail = models.ImageField(blank=False, null=False, upload_to='photos/%y/%m/%d/')
    description = models.TextField(blank=False, null=False, max_length=150)
    body = models.TextField(blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False, default=datetime.now)

    def __str__(self):
        return self.title