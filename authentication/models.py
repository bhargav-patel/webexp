from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	mobile = models.CharField(max_length=15)
	college = models.CharField(max_length=50)
	enroll_no = models.CharField(max_length=12)
	
	def __str__(self):
		return self.user.username+" | "+self.college
		
	def get_top_10(self):
		return Profile.objects.order_by('points')[:10]