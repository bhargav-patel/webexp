from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'(?P<quiz_id>\d+)/waiting$', 'quiz.views.waiting',name='waiting'),
	url(r'(?P<quiz_id>\d+)/getquestion$', 'quiz.views.getquestion'),
	url(r'(?P<quiz_id>\d+)/checkanswer$', 'quiz.views.checkanswer'),
	url(r'(?P<quiz_id>\d+)/uselifeline$', 'quiz.views.uselifeline'),
	url(r'(?P<quiz_id>\d+)/gettop$', 'quiz.views.gettop'),
	url(r'list', 'quiz.views.quiz_list',name='quiz_list'),
	url(r'(?P<quiz_id>\d+)/quiz$', 'quiz.views.quiz',name='quiz'),
)
