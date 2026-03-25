from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Make sure this name matches EXACTLY: UserRegisterForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']