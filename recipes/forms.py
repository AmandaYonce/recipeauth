from django import forms
from .models import Author


class AuthorForm(forms.Form):
    username = forms.CharField(max_length=200)
    bio = forms.CharField(widget=forms.Textarea)
    password=forms.CharField(widget=forms.PasswordInput)


class UserRecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    time_Required = forms.CharField(max_length=200)
    instructions = forms.CharField(widget=forms.Textarea)


class AdminRecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_Required = forms.CharField(max_length=200)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
