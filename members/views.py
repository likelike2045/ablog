from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView

class UserRegisterView(generic.CreateView):

	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):

	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('theblog:home')

	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name='registration/change_password.html'
	success_url = reverse_lazy('theblog:home')
	success_message = "Post was deleted successfully."

	def change(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PasswordsChangeView, self).change(request, *args, **kwargs)



