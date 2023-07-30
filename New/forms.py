from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"

class SubscrimeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    message = forms.CharField()