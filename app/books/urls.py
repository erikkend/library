from django.urls import path
from books.views import SearchBook, BookDetailView, AuthorDetailView, AddBookRating, BookListView

urlpatterns = [
    path('search_book/', SearchBook.as_view(), name='search-book'),
    path('book_list/', BookListView.as_view(), name='book-list'),
    path('book_info/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author_info/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('add-rating/', AddBookRating.as_view(), name='add-rating')
]
