import django_filters
from books.models import Book
from django_filters import DateFilter


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = DateFilter(field_name="pub_date", lookup_expr="gte")
    end_date = DateFilter(field_name="pub_date", lookup_expr="lte")

    class Meta:
        model = Book
        fields = "__all__"
        exclude = ['description', 'pub_date', "price", "image"]
