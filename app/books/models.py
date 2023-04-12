from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    name = models.CharField(blank=False, max_length=200, verbose_name='Имя')
    author = models.ManyToManyField('Author', related_name='author_books', verbose_name='Автор')
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    pub_date = models.DateTimeField('Дата публикации')
    genre = models.ManyToManyField('Genre', related_name='genre_books', blank=False, verbose_name='Жанры')

    def __str__(self):
        return f"{self.name}"

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


class Vote(models.Model):
    RATINGS = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]

    rating = models.PositiveSmallIntegerField(choices=RATINGS, verbose_name='Оценка', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_ratings')
    voted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.name - self.rating}"

    class Meta:
        unique_together = ("user", "book")
