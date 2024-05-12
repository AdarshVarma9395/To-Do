from .models import *
from django.forms import ModelForm
from django import forms


class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'
