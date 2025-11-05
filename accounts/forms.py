# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):    
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:       
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):    
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"})
    )
