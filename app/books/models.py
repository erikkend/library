from django.db import models


class Book(models.Model):
    name = models.CharField(blank=False, max_length=200, verbose_name='Имя')
    author = models.ManyToManyField('Author', related_name='author_books', verbose_name='Автор')
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    pub_date = models.DateTimeField('Дата публикации')

    genre = models.ManyToManyField('Genre', related_name='genre_books', blank=False, verbose_name='Жанры')
    # rating = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
