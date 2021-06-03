from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import userProfile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = userProfile
        fields = ['email', 'user_type'] #'user_name', 'user_type', 'Contact_no', 'Gender', 'Address', 'City', 'State' ,'Country','image'





class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = userProfile
        fields = [ 'user_name',  'Contact_no', 'Gender', 'Address', 'City', 'State' ,'Country','image']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = [ 'user_name',  'Contact_no', 'Gender', 'Address', 'City', 'State' ,'Country','image']