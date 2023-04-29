from django.views import View
from django.db.models import Avg
from books.forms import VoteForm
from cart.forms import CartAddProductForm
from books.models import Book, Author, Vote
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from books.filters import BookFilter


class BookListView(ListView):
    template_name = 'books/searching.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookFilter
        return context

    def get(self, request, *args, **kwargs):
        book_filter = BookFilter(request.GET)
        books = Book.objects.all()

        if book_filter.is_valid():
            book_filter = BookFilter(request.GET, queryset=books)
            books = book_filter.qs
            context = {
                'form': book_filter,
                'object_list': books
            }
            return render(request, self.template_name, context)
        context = {
            'form': book_filter
        }
        return render(request, self.template_name, context)


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VoteForm
        avg_book_rating = self.object.book_ratings.aggregate(Avg("rating"))['rating__avg']
        context['avg_rating'] = avg_book_rating
        context['cart_product_form'] = CartAddProductForm
        return context


class AddBookRating(View):
    def post(self, request):
        form = VoteForm(request.POST)
        if form.is_valid():
            book_id = request.POST.get('book_id')
            book_obj = Book.objects.filter(pk=book_id)[0]
            book_rating = form.cleaned_data['rating']
            Vote.objects.update_or_create(user=request.user, book=book_obj, defaults={"rating": book_rating})
            return redirect('book-detail', pk=book_id)


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
        book_filter = BookFilter(request.POST)
        books = Book.objects.all()

        if book_filter.is_valid():
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
