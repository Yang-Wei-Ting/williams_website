from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput
    )
