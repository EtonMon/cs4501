from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    password = forms.CharField(label='Password', max_length=1000)
    last_name = forms.CharField(label='Last name', max_length=70)
    first_name = forms.CharField(label='First Name', max_length=70)

class SongForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    artists = forms.CharField(label='Artist', max_length=100)

class PoemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    artists = forms.CharField(label='Artist', max_length=100)
    text = forms.CharField(label='Enter Text Here', max_length=10000)

class ImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    artists = forms.CharField(label='Artist', max_length=100)
