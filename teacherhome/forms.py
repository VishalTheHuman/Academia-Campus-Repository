# forms.py
from django import forms
from .models import File

class FileModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['email', 'file', 'permission']