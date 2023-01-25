from .models import Newss
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = Newss
        fields = ['title', 'intro', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Интро'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Статья'
            })
        }