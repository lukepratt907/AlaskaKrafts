from django import forms

from .models import User

class Pic(forms.ModelForm):

    class Meta:
        model = User
        fields = ('image', 'description')

from django.contrib.auth.forms import PasswordResetForm
class MyPasswordResetForm(PasswordResetForm):

    def is_valid(self):
        email = self.data['email']
        if sum([1 for u in self.get_users(email)]) == 0:
            self.add_error(None, "Unknown email; try again.")
            return False
        return super().is_valid()
