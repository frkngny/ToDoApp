from .models import NoteStatus

def get_notes_global_context(request):
    return {'statuses': NoteStatus.objects.all()}