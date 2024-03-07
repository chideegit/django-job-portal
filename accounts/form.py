from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserForm(UserCreationForm):
    """Inheriting from the UserCreationForm class to make magic😊"""
    class Meta:
        model = User 
        fields = ['first_name', 'email', 'password1', 'password2'] # yeah I know I ommitted 'username', check views to see why

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User 
        fields = ['old_password', 'new_password1', 'new_password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name'] # Add your own custom fields if you have any 
        