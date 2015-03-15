from django.db import models

# Create your models here.

class Question(models.Model):
	question = models.CharField(max_length=300,blank=False,null=False)
	image = models.ImageField(blank=True,null=True,upload_to="static/img/que/")
	answer = models.CharField(max_length=20,blank=False,null=False)
	level = models.IntegerField(unique=True)
	options = models.CharField(max_length=50,blank=False,null=False)
	hint = models.CharField(max_length=50,blank=False,null=False)
	link = models.URLField(blank=False,null=False)
	
	def __str__(self):
		return str(self.level)+" "+ self.answer