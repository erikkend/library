from django.contrib import admin
from books.models import Book, Author, Genre, Vote


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Vote)
