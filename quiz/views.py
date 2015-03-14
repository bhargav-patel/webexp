from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your views here.

@login_required
def waiting(request):
	if settings.QUIZ_TIME > datetime.now():
		td = settings.QUIZ_TIME - datetime.now()
		print(td.seconds)
		return render(request,'quiz/waiting.html',{'tds':td.seconds})
	else:
		return redirect(reverse('quiz'))
		
@login_required	
def quiz(request):
	if settings.QUIZ_TIME > datetime.now():
		return redirect(reverse('waiting'))
	else:
		return render(request,'quiz/quiz.html')