from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.forms import ModelForm, Textarea

from .models import Trip, Post


class TripForm(forms.ModelForm):
	class Meta:
		model = Trip
		fields = ('title', 'text', 'date_start', 'date_end', 'country',)
		widgets = {
			'title':forms.Textarea(attrs={'cols': 80, 'rows': 2}),
			'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
		}


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('trip', 'title', 'text', 'url', 'tags',)		
		widgets = {
		
			'title':forms.Textarea(attrs={'cols': 80, 'rows': 2}),
			'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
			'url':forms.Textarea(attrs={'cols': 80, 'rows': 2}),
		}

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30)
	user_email = forms.EmailField(label="Email", help_text='A valid email address, please.')
	password = forms.CharField(label="Password", max_length=30)