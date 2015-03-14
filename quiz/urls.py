from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'waiting$', 'quiz.views.waiting',name='waiting'),
	url(r'$', 'quiz.views.quiz',name='quiz'),
)
