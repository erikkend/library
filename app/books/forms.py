from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(label='Название книги', max_length=200)
