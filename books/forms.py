from django import forms

from .models import User, Profile

class Pic(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image', 'description')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')