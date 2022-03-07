from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    NickName = forms.CharField(max_length=15, required=True)
    RealName = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'NickName', 'RealName')
