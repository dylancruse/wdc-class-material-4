from django import forms
from .models import Book, Author


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.ModelChoiceField(
        # widget=forms.RadioSelect,
        label='Author', queryset=Author.objects.all(), empty_label=None)
    isbn = forms.CharField(label='ISBN', max_length=100)
    popularity = forms.DecimalField(label='Popularity', initial=3.5)


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         exclude = []
