from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import serializers
from quiz.models import Question,Quiz,QuizStats
from django.http import HttpResponse,Http404
import json
from authentication.models import Profile
from django.db.models import Q
from django.utils import timezone
import re

# Create your views here.

@login_required
def waiting(request,quiz_id="-1"):
	q = Quiz.objects.get(id=quiz_id)
	QUIZ_TIME = q.start_time
	if QUIZ_TIME > timezone.now():
		td = QUIZ_TIME - timezone.now()
		return render(request,'quiz/waiting.html',{'tds':td.seconds,'format':'%H : %M : %S','quiz_id':quiz_id})
	else:
		return redirect(reverse('quiz',kwargs={'quiz_id':quiz_id}))
		
@login_required	
def quiz(request,quiz_id="-1"):
	q = Quiz.objects.get(id=quiz_id)
	QUIZ_TIME = q.start_time
	QUIZ_END_TIME = q.end_time
	if QUIZ_TIME > timezone.now():
		return redirect(reverse('waiting',kwargs={'quiz_id':quiz_id}))
	elif QUIZ_END_TIME > timezone.now():
		td = QUIZ_END_TIME - timezone.now()
		return render(request,'quiz/quiz.html',{'tds':td.seconds,'format':'%H : %M : %S','quiz_id':quiz_id})
	else:
		profile = Profile.objects.get(user=request.user)
		try:
			qs = QuizStats.objects.get( Q(user=request.user) & Q(quiz__id=quiz_id) )
		except QuizStats.DoesNotExist:
			qs = QuizStats.objects.create(user=request.user,quiz=q)
		return render(request,'quiz/ended.html',{'profile':profile,'quiz_id':quiz_id,'qs':qs})
		
@login_required	
def getquestion(request,quiz_id="-1"):
	if request.user.is_authenticated():
		q = Quiz.objects.get(id=quiz_id)
		try:
			qs = QuizStats.objects.get( Q(user=request.user) & Q(quiz__id=quiz_id) )
		except QuizStats.DoesNotExist:
			qs = QuizStats.objects.create(user=request.user,quiz=q)
		q = Question.objects.get( Q(quiz__id=quiz_id) & Q(level=qs.level) )
		temp = {
			'quiz_name':qs.quiz.name,
			'level':q.level,
			'question':q.question,
			'points':q.points,
		}
		if q.image:
			temp['image']=q.image.url
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
@login_required		
def checkanswer(request,quiz_id="-1"):
	if request.method == 'POST' and request.user.is_authenticated():
		temp = {
			'status':'error'
		}
		json_data = json.loads(request.body.decode('utf-8'))
		
		qs = QuizStats.objects.get( Q(user=request.user) & Q(quiz__id=quiz_id) )
		
		if json_data.get('level')==qs.level:
			q = Question.objects.get( Q(quiz__id=quiz_id) & Q(level=qs.level) )
			check_ans = ''.join(re.split("\s|,|'|-|\.",json_data.get('answer'))).lower()
			correct_ans = ''.join(re.split("\s|,|'|-|\.",q.answer)).lower()
			if check_ans==correct_ans:
				qs.level = qs.level + 1
				qs.points = qs.points + q.points
				qs.level_up_time = datetime.now()
				qs.save()
				temp['status']='true'
			else:
				temp['status']='false'
		
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
@login_required	
def uselifeline(request,quiz_id="-1"):
	if request.method == 'POST' and request.user.is_authenticated():
		temp = {
			'status':'error'
		}
		json_data = json.loads(request.body.decode('utf-8'))
		type = json_data.get('type')
		level = json_data.get('level')
		temp['type']=type
		
		qs = QuizStats.objects.get( Q(user=request.user) & Q(quiz__id=quiz_id) )
		
		if type==1 and qs.lifeline1==False:
			qs.lifeline1=True
			qs.level = qs.level + 1;
			qs.save()
			temp['status']='success'
		elif type==2 and qs.lifeline2==False:
			qs.lifeline2=True
			qs.points = qs.points-5
			qs.save()
			temp['hint'] = Question.objects.get( Q(quiz__id=quiz_id) & Q(level=qs.level) ).hint
			temp['status']='success'
		elif type==3 and qs.lifeline3==False:
			qs.lifeline3=True
			qs.points = qs.points-5
			qs.save()
			temp['link'] = Question.objects.get( Q(quiz__id=quiz_id) & Q(level=qs.level) ).link
			temp['status']='success'
		else:
			temp['status']='fail'
			
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
@login_required	
def gettop(request,quiz_id="-1"):
	if request.user.is_authenticated():
		top = QuizStats.objects.filter(quiz__id=quiz_id).order_by('-points','-level','level_up_time')[:10]
		
		temp=[]
		for t in top:
			temp.append({"u":t.user.username,"l":t.level,"p":t.points})
		
		try:
			t = QuizStats.objects.get( Q(user=request.user) & Q(quiz__id=quiz_id) )
			temp.append({"u":t.user.username,"l":t.level,"p":t.points})
		except QuizStats.DoesNotExist:
			pass
			
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	raise Http404
	
@login_required
def quiz_list(request):
	q = Quiz.objects.filter(start_time__gte=datetime.now()).order_by('start_time')
	qs = Quiz.objects.filter( Q(start_time__lte=datetime.now()) & Q(end_time__gte=datetime.now()) ).order_by('start_time')
	qc = Quiz.objects.filter( Q(start_time__lte=datetime.now()) & Q(end_time__lte=datetime.now()) ).order_by('start_time')
	return render(request,'quiz/list.html',{'q':q,'qs':qs,'qc':qc})
	
def leaderboard(request,quiz_id):
	if request.method=='POST':
		users = QuizStats.objects.filter(quiz__id=quiz_id)
		temp = []
		for u in users:
			lut = None
			if u.level_up_time:
				lut = u.level_up_time.isoformat()
			temp.append({	"u":u.user.username,
							"n":u.user.first_name+" "+u.user.last_name,
							"l":u.level,
							"p":u.points,
							"c":u.user.profile.college,
							"en":u.user.profile.enroll_no,
							"m":u.user.profile.mobile,
							"em":u.user.email,
							"l1":u.lifeline1,
							"l2":u.lifeline2,
							"l3":u.lifeline3,
							"lut":lut
						})
		data = json.dumps(temp)
		return HttpResponse(data,content_type='application/json')
	else:
		q = Quiz.objects.get(id=quiz_id)
		return render(request,'quiz/leaderboard.html',{'q':q,'quiz_id':quiz_id})