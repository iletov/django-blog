from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	# redirect to page for password change
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
	path('password-success/', views.password_success, name='password_success'),
	path('<int:pk>/user_profile/', ProfilePageView.as_view(), name='user_profile')
]