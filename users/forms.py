from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

# Form for registering a new user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

# Form for updating profile details (The one that was missing!)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'tagline']