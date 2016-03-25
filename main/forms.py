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
