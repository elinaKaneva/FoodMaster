import string
import random

from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean_email(self):

        email = self.cleaned_data.get('email')
        check_email = User.objects.filter(email=email)

        if check_email:
            raise forms.ValidationError(
                "A user associated with this email address already exists")

        return email

    def clean_password(self):
        print(self.cleaned_data)
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        print(password,confirm_password)
        # if not password == confirm_password:
        #     raise forms.ValidationError("Password mismatch")
        #
        # elif len(password) < 6:
        #     raise forms.ValidationError("Password is too short (6 symbols)")
        #
        # elif password.isalpha() or password.isdigit():
        #     raise forms.ValidationError("Password should contain at least one alphabetic and one non-alphabetic character")

        return password

    def save(self):

        data = self.cleaned_data

        new_user = User.objects.create_user(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            )

        return new_user


