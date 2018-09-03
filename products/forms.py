from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from . import models


# Create your models here.
''' Form used in patient registration. Extends UserCreationForm '''
class MyUserRegisterForm(UserCreationForm):
	username = forms.CharField(required=True, label="User Name")
	email = forms.EmailField(required = True, label="Email Address")
	first_name = forms.CharField(required=True, label="First Name")
	last_name = forms.CharField(required=True, label="Last Name")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "first_name",  "last_name")

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
		   raise forms.ValidationError(
			   self.error_messages['password_mismatch'],
			   code='password_mismatch',
		   )
		return password2

	def save(self, commit=True):
		user=super(UserCreationForm, self).save(commit=False)
		user.set_password(self.clean_password2())
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()

		return user




class AddRating(forms.ModelForm):
	
	item_name = forms.CharField(required=True, label="Item Name")
	item_rating = forms.CharField(required = True, label="Rate Item")

	class Meta:
		model=models.Ratings
		fields = ('item_name','item_rating')