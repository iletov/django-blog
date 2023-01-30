from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateProfileForm, PasswordChangingForm, ProfilePageForm, EditProfilePageForm
from myblog.models import Profile



class CreeateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	# fields = '__all__'
	template_name = 'registration/create_user_profile_page.html'

	def form_valid(self, form): # this function inserts the user id into the form
		form.instance.user = self.request.user
		return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
	model = Profile
	form_class = EditProfilePageForm
	template_name = 'registration/edit_profile_page.html'
	# fields = '__all__'
	success_url = reverse_lazy('user_profile')

	# def get_object(self):
	# 	return self.request.user


class ProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	# use the <int:pk>
	def get_context_data(self, *args, **kwargs):
		# users = Profile.objects.all() # Do not need everything
		context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context['page_user'] = page_user
		return context


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

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	# form_class = PasswordChangeView
	success_url = reverse_lazy('password_success')

def password_success(request):
	return render(request, 'registration/password_succes.html', {})