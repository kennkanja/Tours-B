from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ["title","desc","cover"]