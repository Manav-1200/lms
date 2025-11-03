from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a real email address")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "full_name", "role", "password1", "password2")
