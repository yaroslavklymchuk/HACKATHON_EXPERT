from django import forms
from .models import *

class OutputForm(forms.ModelForm):

    class Meta:
        model = Output
        exclude = [""]