from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			# 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

# in case I don't want particular form field, need to create another class like PostForm but without that field
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			# 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			# 'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}