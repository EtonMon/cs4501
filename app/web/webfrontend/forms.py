from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    password = forms.CharField(label='Password', max_length=1000)
    last_name = forms.CharField(label='Last name', max_length=70)
    first_name = forms.CharField(label='First Name', max_length=70)
