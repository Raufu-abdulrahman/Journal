from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Persona, Profile, Journal

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ['name', 'age', 'quote']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']
        


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")
    

class JournalForm(forms.ModelForm):
    
    class Meta:
        model = Journal
        fields = ['title', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
