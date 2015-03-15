from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import serializers
from quiz.models import Question
from django.http import HttpResponse,Http404
import json
from authentication.models import Profile

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
		
def getquestion(request):
	if request.user.is_authenticated():
		profile = Profile.objects.get(user=request.user)
		q = Question.objects.get(level=profile.level)
		temp = {
			'level':q.level,
			'question':q.question,
			'image':q.image.url,
		}
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
		
def checkanswer(request):
	print(request.is_ajax())
	if request.method == 'POST' and request.user.is_authenticated():
		temp = {
			'status':'error'
		}
		json_data = json.loads(request.body)
		
		profile = Profile.objects.get(user=request.user)
		
		if json_data.get('level')==profile.level:
			q = Question.objects.get(level=profile.level)
			if json_data.get('answer')==q.answer:
				profile.level = profile.level + 1;
				profile.save()
				temp['status']='true'
			else:
				temp['status']='false'
		
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404