from django import forms
from ramya.models import ram

class rammy(forms.ModelForm):
    class Meta:
        model=ram
        exclude=[]