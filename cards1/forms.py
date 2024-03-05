from django import forms
from cards1.models import Movie

#form definition
class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"


