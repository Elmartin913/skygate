from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Author, Book, Tag, GENRES


class BookCreatorStep1Form(forms.Form):
    title = forms.CharField(label='Title', max_length=256)
    gender = forms.ChoiceField(label='Gender', choices=GENRES)
    isbn = forms.CharField(label='ISBN number', max_length=17)
    author = forms.ModelChoiceField(label='Author', queryset=Author.objects.all())


class BookCreatorStep2Form(forms.Form):
    first_name = forms.CharField(label='First name', max_length=256)
    last_name = forms.CharField(label='Last name', max_length=256)


# account
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
