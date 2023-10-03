from django import forms

class NewTaskForm(forms.Form):
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password")
    password2 = forms.CharField(label="Confirm Password")

    def clean(self):
        super(NewTaskForm, self).clean()

        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            self.errors['password1'] = self.error_class([
                'Passwords must be the same'
            ])
        return self.cleaned_data
