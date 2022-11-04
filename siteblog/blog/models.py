from django.db import models
from django.urls import reverse

'''
Category
-----------
title, slug(алиас для url)

Tag
-----------
title, slug

Post
-----------
title, slug, author, content, created_at, photo, views, category, tags
'''

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url_cat', unique=True)

    def __str__(self):                        # служебный метод, возвращает строковый title объекта модели
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:                               # всякие доп параметры
        verbose_name = 'Категория(ю)'            # для отображения в админке
        verbose_name_plural = 'Категории'
        ordering = ['title']                  # порядок сортировки

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url_tag', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'  # для отображения в админке
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url_post', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')     # У класса Post появится св-во category, а у класса Category появиться свойство posts
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')                       # У модели Tag появиться свойство posts  ManyToMany создает еще одну таблицу связующую

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'  # для отображения в админке
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']