from django.urls import path
from books.views import SearchBook, BookDetailView, AuthorDetailView

urlpatterns = [
    path('search_book/', SearchBook.as_view(), name='search-book'),
    path('book_info/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author_info/<int:pk>', AuthorDetailView.as_view(), name='author-detail')
]
