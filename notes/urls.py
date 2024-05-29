from django.urls import path, include
from .views import home, create_note, UserNotesList

urlpatterns = [
    path('', home, name='notes-home'),
]

htmxpatterns = [
    path('user-notes', UserNotesList.as_view, name='user-notes'),
    path('create-note', create_note, name='create-note')
]

urlpatterns += htmxpatterns

