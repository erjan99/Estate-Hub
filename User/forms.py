from idlelib.debugobj import myrepr

from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import MyUser

class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email')


class MyUserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
