from django import forms
from .models import Partcipant


class RegisterationForm(forms.Form):
    email = forms.EmailField(label="Your Email")
