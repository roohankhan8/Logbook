# forms.py
from django import forms
from .models import *

class CreateLogbookForm(forms.ModelForm):
    class Meta:
        model = Logbook
        fields = ['title']  # Add fields you want the user to input

class JoinLogbookForm(forms.Form):
    logbook_code = forms.CharField(max_length=8)
