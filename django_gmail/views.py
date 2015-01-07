import httplib2
import logging
import pytz
import random
import re
import time
import urllib
import base64
from datetime import datetime, date, timedelta
from email.mime.text import MIMEText

from apiclient.discovery import build
from apiclient.errors import HttpError

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc, make_aware, get_current_timezone

from oauth2client import xsrfutil
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from oauth2client.django_orm import Storage

FLOW = OAuth2WebServerFlow(client_id=settings.GA_CLIENT_ID,
						   client_secret=settings.GA_CLIENT_SECRET,
						   scope=settings.GA_SCOPE,
						   redirect_uri=settings.GOOGLE_REDIRECT_URI)

@login_required
def gmail_oauth_callback(request):
	""" Google API oauth2 callback route
		https://developers.google.com/api-client-library/python/guide/django
	"""
	internal_contact = None
	code = request.REQUEST.get('code')
	state = request.REQUEST.get('state')
	user = request.user
		
	#if not xsrfutil.validate_token(settings.SECRET_KEY, state, user):
		#print "token not valid"
		#return HttpResponseBadRequest()
		
	# if user denies access redirect to activate
	if request.GET.get('error') != 'access_denied':
		try:
			credentials = FLOW.step2_exchange(request.REQUEST)
		except FlowExchangeError, exc:
			raise Http404
						
		http = httplib2.Http()
		http = credentials.authorize(http)
		service = build('gmail', 'v1', http=http)
		profile = service.users().getProfile(userId="me").execute()
					
		creds,_ = GoogleCredentials.objects.get_or_create(user=request.user)
		creds.credentials = credentials
		creds.save()
		
	return redirect(settings.GMAIL_POST_AUTH_REDIRECT)
