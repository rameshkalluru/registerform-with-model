from django import forms
from apphello.models import registermodel

class women(forms.ModelForm):
    class Meta:
        model=registermodel
        exclude=[]