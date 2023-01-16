from django.shortcuts import render
from django.http import Http404
from .models import Note
from django.views.generic import ListView, DetailView, CreateView
from .forms import NoteForm



class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'


class NotesCreateView(CreateView):
    model = Note
    # fields = ['title', 'text']
    form_class = NoteForm
    success_url = '/smart/notes'