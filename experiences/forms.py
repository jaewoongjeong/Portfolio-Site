from django import forms
from .models import PostModel
from django_summernote.widgets import SummernoteWidget


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),
        }
        help_texts = {
            'slug': 'It uses blog title to create an unique url',
            'anonymous': "Clicking on this box won't disclose your ID anywhere on this website",
            'tags': 'How to include Tags?',
        }