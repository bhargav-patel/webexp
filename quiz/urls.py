from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'waiting$', 'quiz.views.waiting',name='waiting'),
	url(r'getquestion$', 'quiz.views.getquestion',name='quiz'),
	url(r'$', 'quiz.views.quiz',name='quiz'),
)
