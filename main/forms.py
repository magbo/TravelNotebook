from django import forms

from .models import Trip, Post, Tag


class TripForm(forms.ModelForm):

	class Meta:
		model = Trip
		fields = ('title', 'text', 'date_start', 'date_end', 'country',)

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('trip', 'title', 'text', 'url', 'tags',)		
				
