from django import forms
from .models import Post, Category

# 1 - Hardcoding the category will be like:
# categories = [('random', 'random'), ('sports', 'sports'), ('social', 'social')]

# 2 - dynamic:
categories = Category.objects.all().values_list('name', 'name')
list_categories = []

for item in categories:
	list_categories.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'snippet', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			# 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'ivan', 'type':'hidden'}),
			# 'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=list_categories, attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),


		}

# in case I don't want particular form field, need to create another class like PostForm but without that field
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'snippet', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			# 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			# 'author': forms.Select(attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}