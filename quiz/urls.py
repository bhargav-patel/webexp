from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'waiting$', 'quiz.views.waiting',name='waiting'),
	url(r'ended$', 'quiz.views.ended',name='ended'),
	url(r'getquestion$', 'quiz.views.getquestion'),
	url(r'checkanswer$', 'quiz.views.checkanswer'),
	url(r'uselifeline$', 'quiz.views.uselifeline'),
	url(r'gettop$', 'quiz.views.gettop'),
	url(r'$', 'quiz.views.quiz',name='quiz'),
)
