
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    first_name = forms.CharField(label="Křestní jméno", max_length=30, required=True, help_text="Required.")
    last_name = forms.CharField(label="Příjmení", max_length=30, required=True, help_text="Required.")
    email = forms.EmailField(label="E-mail")
    gender = forms.ChoiceField(label="Oslovení", choices=[(1, "Pán"), (2, "Paní")])
    password = forms.CharField(label="Heslo", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Potvrďte heslo", widget=forms.PasswordInput)




