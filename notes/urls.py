from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
]

htmxpatterns = [
    path('user-notes', views.UserNotesList.as_view, name='user-notes'),
    path('create', views.create_note, name='create-note'),
    path('delete/<int:pk>', views.delete_note, name='delete-note')
]

urlpatterns += htmxpatterns

