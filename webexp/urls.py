from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webexp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/', include('authentication.urls')),
	url(r'^quiz/', include('quiz.urls')),
	url(r'^$', 'quiz.views.quiz',name='quiz'),
)
