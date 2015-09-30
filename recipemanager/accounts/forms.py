from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'
        )

    def clean_password(self):
        pw = self.cleaned_data['password']
        if len(pw) < 6:
            raise forms.ValidationError('Password must be at least 7 characters long')
        elif not has_capital(pw):
            raise forms.ValidationError('Password must have capital letter')
        return pw

    def clean_password2(self):
        pw = self.cleaned_data.get('password')
        pw2 = self.cleaned_data['password2']
        if not pw:
            return pw2
        if pw != pw2:
            raise forms.ValidationError('Passwords do not match!')
        return pw2

    def save(self):
        new_user = super(UserForm, self).save()

        pw = self.cleaned_data['password1']
        new_user.set_password(pw)
        new_user.save()
        return new_user
