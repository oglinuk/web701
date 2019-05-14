from django import forms
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'email',
            'address',
            'phone'
        )