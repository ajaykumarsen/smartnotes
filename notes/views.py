from django.shortcuts import render
from django.http import Http404
from .models import Note
# Create your views here.

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note Doesn't Exist!")
    return render(request, 'notes/notes_detail.html', {'note': note})