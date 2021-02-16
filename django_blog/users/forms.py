from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserPasswordResetForm(PasswordResetForm):
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        user = User.objects.filter(email=cleaned_data.get('email')).first()
        if user is None:
            self.add_error('email', 'Account not found for this email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
