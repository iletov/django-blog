from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile


class SignUpForm(UserCreationForm):
	# to use bootstrap insert --> widget=forms.NameInput(attrs={'class': 'form-control'})
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		# inherit from the parrent class and add bootstrap to the username and pasword fields
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'



class UpdateProfileForm(UserChangeForm):
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	# last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# is_superuser = forms.CharField(widget=forms.ChechboxInput(attrs={'class': 'form-chech'}))
	# is_staff = forms.CharField(widget=forms.ChechboxInput(attrs={'class': 'form-chech'}))
	# is_active = forms.CharField(widget=forms.ChechboxInput(attrs={'class': 'form-chech'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordChangingForm(PasswordChangeForm):
	# to use bootstrap insert --> widget=forms.NameInput(attrs={'class': 'form-control'})
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')


class EditProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'github_url', 'twitter_url', 'linkedin_url')
		
		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			# 'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			'github_url': forms.TextInput(attrs={'class': 'form-control'}),
			'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
			'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
			}


class ProfilePageForm(forms.ModelForm):	
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'github_url', 'twitter_url', 'linkedin_url')

		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			# 'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title text'}),
			'github_url': forms.TextInput(attrs={'class': 'form-control'}),
			'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
			'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
			}