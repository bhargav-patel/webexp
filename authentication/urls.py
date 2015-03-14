from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'register/', 'authentication.views.register',name='register'),
    url(r'login/', 'authentication.views.login_view',name='login'),
)