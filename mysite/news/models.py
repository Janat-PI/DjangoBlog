from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='get_news')
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def get_absolute_url(self):
        return reverse_lazy('new-detail', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Category name', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title
