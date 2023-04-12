from django import forms
from django.forms import ModelForm
from books.models import Vote


class SearchForm(forms.Form):
    name = forms.CharField(label='Название книги', max_length=200)


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['rating']
