from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm


@login_required
def home(request):
    return render(request, 'notes/home.html', {'form': NoteForm, 'notes': request.user.notes.all()})


class UserNotesList(ListView, LoginRequiredMixin):
    template_name = 'notes/home.html'
    model = Note
    context_object_name = 'note'
    
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return user.notes.all()
    
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return render(request, 'notes/notes_list.html', {'notes': request.user.notes.all()})
        else:
            return HttpResponse(form.errors.__str__())