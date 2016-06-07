from django import forms
from scrape.models import Attendance, Gpalist, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter the username.")
    email = forms.CharField(help_text="Please enter the email.")
    password = forms.CharField(
        widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    regno = forms.CharField(help_text="Please enter the registration number.")
    dob = forms.CharField(help_text="Please enter the DOB in YYYY-MM-DD format.")

    class Meta:
        model = UserProfile
        fields = ('regno', 'dob')
