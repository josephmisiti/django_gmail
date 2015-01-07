import datetime
import decimal
import json
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User

from oauth2client.django_orm import CredentialsField
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ['oauth2client.django_orm.CredentialsField'])


class GoogleCredentials(TimeStampedModel):

	user = models.ForeignKey(User)
	credentials = CredentialsField()
	edited_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'GoogleCredentials user_id=%s'  % self.user.id

	class Meta:
		db_table = 'users_google_credentials'
		verbose_name_plural = 'Google Credentials'
