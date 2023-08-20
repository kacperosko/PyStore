# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            # attrs={
            #     "class": "login-input"
            # }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            # attrs={
            #     "class": "login-input"
            # }
        ))


class SignUpForm(UserCreationForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False
