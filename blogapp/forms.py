from django import forms
from .models import upload
from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','password','email','first_name','last_name']
        widgets={'password':forms.PasswordInput()}

class uploadform(forms.ModelForm):
    class Meta:
        model=upload
        fields=['Title','Description','name','pic']
