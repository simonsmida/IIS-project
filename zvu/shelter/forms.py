from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login")
       

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError(
                "new_password and confirm_password does not match"
            )


class ChangeAccForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]