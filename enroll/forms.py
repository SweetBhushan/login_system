from attr import field
from django import forms
from django import forms
from .models import studentRegistration

class studentform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = studentRegistration
        fields='__all__'

