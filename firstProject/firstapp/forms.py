##model form
from django.forms import ModelForm
from .models import Users
from django import forms

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = {'first_name', 'last_name'}