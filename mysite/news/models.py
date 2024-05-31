from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название новости')
    content = models.TextField(blank=True, verbose_name='Текст новости')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')  
    is_published=models.BooleanField(default=True, verbose_name='Опубликована')
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True,verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['-created_at']


class Category(models.Model):  
    title=models.CharField(max_length=150, verbose_name='Название категории', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']







