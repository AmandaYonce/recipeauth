from django import forms
from .models import Author


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=200)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_Required = forms.CharField(max_length=200)
    instructions = forms.CharField(widget=forms.Textarea)