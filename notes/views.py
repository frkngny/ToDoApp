from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Note
from .forms import NoteForm


def home(request):
    return render(request, 'notes/home.html', {'form': NoteForm})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return HttpResponse({'note': note})
        else:
            return HttpResponse({'error': 'Error occured.'})

def get_user_notes(request):
    if request.method == 'GET':
        user_notes = Note.objects.filter(user=request.user)
        return render(request, 'notes/notes_list.html', {'notes': user_notes})