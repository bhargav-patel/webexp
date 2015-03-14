from django.shortcuts import render,redirect
from authentication.forms import UserForm,ProfileForm,LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.user.is_authenticated():
		return redirect(reverse('waiting'))
	if request.POST:
		userform = UserForm(request.POST)
		userprofileform = ProfileForm(request.POST)
		if userform.is_valid() and userprofileform.is_valid():
			user = userform.save()
			userprofile = userprofileform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return redirect(reverse('login'))
	else:
		userform = UserForm()
		userprofileform = ProfileForm()
	return render(request,'auth/register.html',{'userform':userform,'userprofileform':userprofileform})
	
def login_view(request):
	error=None
	next = request.GET.get('next',None)
	if request.user.is_authenticated():
		return redirect(reverse('waiting'))
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			
			if user is not None:
				login(request,user)
				if request.GET.get('next') is not None:
					print('here')
					return redirect(request.GET["next"])
				return redirect(reverse('waiting'))
		
		error='Invalid credentials.'
		
	else:
		form = LoginForm()
		
	
		
	return render(request,'auth/login.html',{'form':form,'error':error,'next':next})
	
@login_required	
def logout_view(request):
	logout(request)
	return redirect(reverse('login'))
