from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Note, NoteStatus
from .forms import NoteForm, NoteEditForm


@login_required
def home(request):
    return render(request, 'notes/home.html', {'create_form': NoteForm, 'notes': request.user.notes.all()})


class UserNotesList(ListView, LoginRequiredMixin):
    template_name = 'notes/home.html'
    model = Note
    context_object_name = 'note'
    
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return user.notes.all()

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.status = NoteStatus.objects.get(name='ToDo')
            note.save()
            return render(request, 'notes/notes_list.html', {'notes': request.user.notes.all()})
        else:
            return HttpResponse(form.errors.__str__())

@login_required
def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    edit_form = NoteEditForm(instance=note)
    if request.method == 'POST':
        filled_edit_form = NoteEditForm(request.POST, instance=note)
        if filled_edit_form.is_valid():
            filled_edit_form.save()
            edit_form = filled_edit_form
    else:
        return render(request, 'notes/edit_note.html', {'editable_note': note, 'edit_form': edit_form})

@login_required
def delete_note(request, pk):
    request.user.notes.get(pk=pk).delete()
    return render(request, 'notes/notes_list.html', {'notes': request.user.notes.all()})

