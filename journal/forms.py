from django import forms
from .models import JournalEntry, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['content']

class RegisterForm(UserCreationForm):
    theme = forms.ChoiceField(
        choices=Profile.THEME_CHOICES,
        widget = forms.Select(attrs={'class': 'theme-select'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'theme']