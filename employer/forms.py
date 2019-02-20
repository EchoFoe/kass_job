from django import forms
from .models import *


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ["created", "updated"]