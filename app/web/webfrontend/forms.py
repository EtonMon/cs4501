from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=40)
    password = forms.CharField(label='Password', max_length=100)
    lastname = forms.CharField(label='Last name', max_length=70)
    firstname = forms.CharField(label='First Name', max_length=70)
