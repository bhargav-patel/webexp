from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webexp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adminp/', include(admin.site.urls)),
	url(r'^auth/', include('authentication.urls')),
	url(r'^quiz/', include('quiz.urls')),
	url(r'^about/', TemplateView.as_view(template_name='about.html'),name='about'),
	url(r'^$','quiz.views.quiz_list',name='home'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
