# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'user_type', 'roll_number', 'teacher_id', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
