from django.db import models


class Book(models.Model):
    name = models.CharField(blank=False, max_length=200, verbose_name='Имя')
    author = models.ManyToManyField('Author', related_name='books', verbose_name='Автор')
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    pub_date = models.DateTimeField('Дата публикации')

    # genre = models.Choices() доработать
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
