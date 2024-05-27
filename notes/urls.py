from django.urls import path, include
from .views import home, create_note, get_user_notes

urlpatterns = [
    path('', home, name='notes-home'),
    path('/create', create_note, name='note-create'),
]

htmxpatterns = [
    path('/user_notes', get_user_notes, name='user-notes'),
]

urlpatterns += htmxpatterns

