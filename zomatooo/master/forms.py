from django import forms
from django.contrib.auth.models import User
from .models import *

class MasterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {'password': forms.PasswordInput}
        help_texts ={'username':''}


class ItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields='__all__'

        

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['item_id']