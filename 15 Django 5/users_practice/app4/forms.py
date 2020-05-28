from django import forms
from django.contrib.auth.models import User
from app4.models import UserInfo

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('website','profile_pic') # check the field name correctly
