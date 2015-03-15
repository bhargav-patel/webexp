from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	mobile = models.CharField(max_length=10)
	level = models.IntegerField(default=1)
	lifeline1 = models.BooleanField(default=False)
	lifeline2 = models.BooleanField(default=False)
	lifeline3 = models.BooleanField(default=False)
	