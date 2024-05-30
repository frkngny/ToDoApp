from django.db import models
from django.contrib.auth.models import User


class NoteStatus(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    duedate = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(NoteStatus, on_delete=models.CASCADE, blank=True, null=True)