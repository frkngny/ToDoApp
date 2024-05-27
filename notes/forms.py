from django import forms

from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=True,
                            error_messages={'required': 'Title cannot be empty'})
    class Meta:
        model = Note
        fields = ['title', 'body']
        labels = {'title': 'Title', 'body': 'Body'}
        