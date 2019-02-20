from django import forms
from .models import *


class Job_seekerForm(forms.ModelForm):
    class Meta:
        model = Job_seeker
        exclude = ["created", "updated"]