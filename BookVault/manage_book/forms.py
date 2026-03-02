from django import forms
from .models import Book

Language_Choices = [
    ('EN', 'English'),
    ('HI', 'Hindi'),
    ('FR', 'French')
]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'published_date':forms.DateInput(attrs={
                'type':'Date'
            }),
            'language':forms.Select(choices=Language_Choices),
            'description':forms.Textarea(attrs={
                'rows':'3',
            })
        }