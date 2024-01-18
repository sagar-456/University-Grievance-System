# forms.py
from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complaint, UserResponse

 


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title','post_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Title'}),
            'post_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your complaint here...'})
            }


class ResponseForm(forms.ModelForm):
    notice_id = forms.IntegerField(widget=forms.HiddenInput())  

    class Meta:
        model = UserResponse
        fields = ['notice_id','response']
        widgets = {
            'response': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your Response here...'}),
        }


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    phone_number = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))

    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'), 
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': ' form-check form-check-inline'}))

    USER_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Teaching Staff', 'Teaching Staff'),
        ('Non-teaching Staff', 'Non-teaching Staff'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select form-select-lg mt-2 p-3'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'password1', 'password2', 'user_type')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg mt-3'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'