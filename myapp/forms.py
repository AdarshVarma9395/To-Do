from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
