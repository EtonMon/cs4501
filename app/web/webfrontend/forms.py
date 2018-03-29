from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

    helper = FormHelper()
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('password', css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    password = forms.CharField(label='Password', max_length=1000, widget=forms.PasswordInput())
    last_name = forms.CharField(label='Last name', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)

    helper = FormHelper()
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('password', css_class='input-xlarge'),
        Field('first_name', css_class='input-xlarge'),
        Field('last_name', css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )

class StoryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    artists = forms.CharField(label='Artist', max_length=100)
    text = forms.CharField(label='Description',
        widget = forms.Textarea(),
    )

    helper = FormHelper()
    helper.layout = Layout(
        Field('title', css_class='input-xlarge'),
        Field('artists', css_class='input-xlarge'),
        Field('text', rows="4", css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )

class PoemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    artists = forms.CharField(label='Artist', max_length=100)
    text = forms.CharField(label='Description',
        widget = forms.Textarea(),
    )

    helper = FormHelper()
    helper.layout = Layout(
        Field('title', css_class='input-xlarge'),
        Field('artists', css_class='input-xlarge'),
        Field('text', rows="4", css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )

class MusicVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    artists = forms.CharField(label='Artist', max_length=100)

class SongForm(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    artists = forms.CharField(label='Artist', max_length=100)

class ImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    artists = forms.CharField(label='Artist', max_length=100)
