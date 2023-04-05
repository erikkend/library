from django.shortcuts import render
from django.views import View
from books.models import Book, Author
from books.forms import SearchForm
from django.views.generic.detail import DetailView


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class SearchBook(View):
    template_name = 'books/search_result.html'

    def get(self, request):
        context = {
            'form': SearchForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SearchForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            books = Book.objects.filter(name__icontains=name)
            context = {
                'form': form,
                'books': books
            }
            return render(request, self.template_name, context)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
