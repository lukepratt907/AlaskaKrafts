from django import forms

from .models import User

class Pic(forms.ModelForm):

    class Meta:
        model = User
        fields = ('image', 'description')