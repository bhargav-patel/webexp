from django.shortcuts import render,redirect
from authentication.forms import UserForm,ProfileForm
from django.core.urlresolvers import reverse

# Create your views here.

def register(request):
	if request.user.is_authenticated():
		return redirect('/admin/')
	if request.POST:
		userform = UserForm(request.POST)
		userprofileform = ProfileForm(request.POST)
		if userform.is_valid() and userprofileform.is_valid():
			user = userform.save()
			userprofile = userprofileform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return redirect('/admin/')
	else:
		userform = UserForm()
		userprofileform = ProfileForm()
	return render(request,'auth/register.html',{'userform':userform,'userprofileform':userprofileform})
