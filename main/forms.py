from django import forms

from .models import Trip, Post, Tag


class TripForm(forms.ModelForm):
	class Meta:
		model = Trip
		fields = ('title', 'image', 'country', 'text', 'date_start', 'date_end')
		widgets = {
		}

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ('value',)

		

class PostForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		owner = kwargs.pop('user')
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['trip'].queryset = self.fields['trip'].queryset.filter(owner=owner)
		self.fields['tags'].queryset = self.fields['tags'].queryset.filter(owner=owner)

	class Meta:
		model = Post
		fields = ('trip', 'title', 'text', 'url', 'image', 'place', 'tags')
		


