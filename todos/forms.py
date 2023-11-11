
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    gender = forms.ChoiceField(label="Oslovení", choices=[(1, "Pán"), (2, "Paní")])
    password = forms.CharField(label="Heslo", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Potvrďte heslo", widget=forms.PasswordInput)




