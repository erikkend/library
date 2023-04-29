from books.models import Book, Author
import django_filters
from django_filters import widgets


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='', lookup_expr='icontains', widget=django_filters.widgets.forms.TextInput(attrs={'class': 'form-control filter-name', 'placeholder': 'Поиск'}))
    price = django_filters.RangeFilter(label='Цена', widget=django_filters.widgets.RangeWidget(attrs={'class': 'mt-3 filter-price'}))
    author = django_filters.ModelMultipleChoiceFilter(label='Авторы', queryset=Author.objects.all(), to_field_name="id", widget=django_filters.widgets.forms.SelectMultiple(attrs={'class': 'form-control filter-author'}))

    class Meta:
        model = Book
        fields = ["name", "author", "price"]
