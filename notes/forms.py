from django import forms

from .models import Note, NoteStatus

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=True,
                            error_messages={'required': 'Title cannot be empty'})
    
    class Meta:
        model = Note
        fields = ['title', 'body', 'duedate']
        labels = {'title': 'Title', 'body': 'Body', 'duedate': 'Due Date'}
        widgets = {
            'duedate':forms.TextInput(attrs={'type':'datetime-local'}),
        }
        

class NoteEditForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=True,
                            error_messages={'required': 'Title cannot be empty'})
    status = forms.ModelChoiceField(queryset=NoteStatus.objects, empty_label=None)
    class Meta:
        model = Note
        fields = ['title', 'body', 'status', 'duedate']
        labels = {'title': 'Title', 'body': 'Body', 'status': 'Status', 'duedate': 'Due Date'}
        widgets = {
            'duedate':forms.TextInput(attrs={'type':'datetime-local'}),
        }