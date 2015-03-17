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
		return render(request,'quiz/waiting.html',{'tds':td.seconds,'format':'%H : %M : %S'})
	else:
		return redirect(reverse('quiz'))
		
@login_required	
def quiz(request):
	if settings.QUIZ_TIME > datetime.now():
		return redirect(reverse('waiting'))
	elif settings.QUIZ_END_TIME > datetime.now():
		td = settings.QUIZ_END_TIME - datetime.now()
		return render(request,'quiz/quiz.html',{'tds':td.seconds,'format':'%H : %M : %S'})
	else:
		profile = Profile.objects.get(user=request.user)
		return render(request,'quiz/ended.html',{'profile':profile})
		
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
	if request.method == 'POST' and request.user.is_authenticated():
		temp = {
			'status':'error'
		}
		json_data = json.loads(request.body)
		
		profile = Profile.objects.get(user=request.user)
		
		if json_data.get('level')==profile.level:
			q = Question.objects.get(level=profile.level)
			if json_data.get('answer')==q.answer:
				profile.level = profile.level + 1
				profile.points = profile.points + q.points
				profile.save()
				temp['status']='true'
			else:
				temp['status']='false'
		
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
def uselifeline(request):
	if request.method == 'POST' and request.user.is_authenticated():
		temp = {
			'status':'error'
		}
		json_data = json.loads(request.body)
		type = json_data.get('type')
		level = json_data.get('level')
		temp['type']=type
		
		profile = Profile.objects.get(user=request.user)
		
		if type==1 and profile.lifeline1==False:
			profile.lifeline1=True
			profile.level = profile.level + 1;
			profile.save()
			temp['status']='success'
		elif type==2 and profile.lifeline2==False:
			profile.lifeline2=True
			profile.save()
			temp['hint']=Question.objects.get(level=level).hint
			temp['status']='success'
		elif type==3 and profile.lifeline3==False:
			profile.lifeline3=True
			profile.save()
			temp['link']=Question.objects.get(level=level).link
			temp['status']='success'
		else:
			temp['status']='fail'
			
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
def gettop(request):
	if request.user.is_authenticated():
		top = Profile.objects.order_by('-points')[:10]
		temp=[]
		for t in top:
			temp.append({"u":t.user.username,"l":t.level,"p":t.points})
		t = Profile.objects.get(user=request.user)
		temp.append({"u":t.user.username,"l":t.level,"p":t.points})
		
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404