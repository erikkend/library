from django.shortcuts import render
from django.views import View
from books.models import Book, Author
from books.forms import SearchForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from books.filters import BookFilter


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class SearchBook(View):
    template_name = 'books/search_result.html'

    def get(self, request):
        book_filter = BookFilter(request.GET)
        context = {
            'form': book_filter
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # form = SearchForm(data=request.POST)
        book_filter = BookFilter(request.POST)
        books = Book.objects.all()

        if book_filter.is_valid():
            print(book_filter.data)
            book_filter = BookFilter(request.POST, queryset=books)
            books = book_filter.qs
            context = {
                'form': book_filter,
                'books': books
            }
            return render(request, self.template_name, context)
        context = {
            'form': book_filter
        }
        return render(request, self.template_name, context)