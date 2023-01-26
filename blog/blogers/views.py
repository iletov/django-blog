from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateProfileForm


class UserRegisterView(generic.CreateView):
	# form_class = UserCreationForm
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


# Update the users info
class UserEditView(generic.UpdateView):
	form_class = UpdateProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	# Get the current users infrmation to update
	def get_object(self):
		return self.request.user

