from django import forms
from django.contrib.auth.models import User
from .models import Signup

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Signup
        fields = ('first_name', 'last_name', 'email', 'gender', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user = User.objects.create_user(
            username=self.cleaned_data['email'],  # Assuming email as username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
