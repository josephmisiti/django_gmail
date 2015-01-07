from __future__ import unicode_literals
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns("",
	url(r'^oauthcallback$', GoogleClient.auth_callback, name='google-oauth-callback'),	
)