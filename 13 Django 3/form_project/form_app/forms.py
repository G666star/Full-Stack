from django import forms
from django.core import validators
# from django.core.exceptions import ValidationError

def mast(value):
    if 'maal' not in value:
        raise forms.ValidationError('maal chahiye')


class UserForm(forms.Form):
    name = forms.CharField(validators=[mast])
    email = forms.EmailField()
    textrty = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
