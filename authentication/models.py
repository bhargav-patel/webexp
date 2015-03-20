from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	mobile = models.CharField(max_length=10)
	level = models.IntegerField(default=1)
	points = models.IntegerField(default=0)
	lifeline1 = models.BooleanField(default=False)
	lifeline2 = models.BooleanField(default=False)
	lifeline3 = models.BooleanField(default=False)
	level_up_time = models.DateTimeField(null=True,blank=True)
	
	def __str__(self):
		return self.user.username+" < "+str(self.level)+" >  < "+str(self.points)+" >"
		
	def get_top_10(self):
		return Profile.objects.order_by('points')[:10]