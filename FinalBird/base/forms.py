from django import forms
from .models import Task

class StatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['data']