from django import forms
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class UserRegisterForm(forms.ModelForm):
    #Student_Name= forms.CharField(max_length=300)
    email = forms.EmailField(label="Email Address")
    email2 = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['username','password','password2','email','email2']

    def clean_password2(self):
        print(self.cleaned_data)
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password, password2)
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            return password
    
    def clean_email2(self):
        print(self.cleaned_data)
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        print(email, email2)
        if email != email2:
            raise forms.ValidationError("Email addresses don't match")
        email_qs = User.objects.filter(email=email)
        if  email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        else:
            return email


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        #user_qs = User.objects.filter(username=username)
        #if user_qs.count() == 1:
        #   user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
            return super(UserLoginForm, self).clean(*args, **kwargs)
                        
    def clean_remember_me(self):
        """clean method for remember_me """
        remember_me = self.cleaned_data.get['remember_me']
        if not remember_me:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        else:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
            return remember_me



class AdvertForm(forms.ModelForm):
    class Meta:
        model = ajax
        fields = '__all__'