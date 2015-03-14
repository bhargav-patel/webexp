from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'$', 'quiz.views.waiting',name='waiting'),
)
