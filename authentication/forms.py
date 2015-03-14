from django import forms
from authentication.models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(required=True,widget=forms.PasswordInput())
	password2 = forms.CharField(required=True,widget=forms.PasswordInput,label="Password(Again)")
	
	class Meta:
		model = User
		fields = ['first_name','last_name','username','password','password2','email']
		
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True
		
	def clean(self):
		cleaned_data=super(UserForm,self).clean()
		print('here')
		pass1 = cleaned_data.get('password')
		pass2 = cleaned_data.get('password2')
		if pass1!=pass2:
			raise forms.ValidationError('Passwords did not match.')
		return cleaned_data
		
	def save(self,commit=True):
		user = super(UserForm,self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		user.save(commit)
		return user
		
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['mobile']