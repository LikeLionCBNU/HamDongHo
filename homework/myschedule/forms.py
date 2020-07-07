from django import forms
from .models import Schedule

class PostForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = {'title', 'memo','schedule_date',}