from django.contrib import admin

from .models import Note, NoteStatus

admin.site.register(Note)
admin.site.register(NoteStatus)
