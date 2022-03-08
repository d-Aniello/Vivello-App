from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='User')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


def pass_length_validation(value):
    if len(value)<9:
        raise ValidationError('Hasło jest za krótkie')


class RegistrationForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])
    pass_2 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])

    class Meta:
        model = User
        fields = [
            'username',
            'pass_1',
            'pass_2'
        ]

    def clean(self):
        data = super().clean()
        if data.get('pass_1') != data.get('pass_2'):
            raise ValidationError('Hasła nie są identyczne')
        return data


class UserPermissionForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ['user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }