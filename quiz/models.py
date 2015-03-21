from django.db import models

# Create your models here.

class Question(models.Model):
	question = models.CharField(max_length=300,blank=False,null=False)
	image = models.ImageField(upload_to="static/img/que/",blank = True)
	answer = models.CharField(max_length=20,blank=False,null=False)
	level = models.IntegerField(unique=True)
	options = models.CharField(max_length=50,blank=False,null=False)
	hint = models.CharField(max_length=50,blank=False,null=False)
	link = models.URLField(blank=False,null=False)
	points = models.IntegerField()
	
	def __str__(self):
		return str(self.level)+" "+ self.answer
		
class QuizTime(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	name = models.CharField(max_length=50,default='Quiz')
	
	def __str__(self):
		return str(self.start_time)+" "+str(self.end_time)