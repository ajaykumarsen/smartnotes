from django import forms
from django.core.exceptions import ValidationError
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title'] # will get title from cleaned_data which is a dict.
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django')
        return title
