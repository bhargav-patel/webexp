from django.db import models
from django.contrib.auth.models import User

# Create your models here.
		
class Quiz(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	name = models.CharField(max_length=50,default='Quiz')
	
	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	question = models.CharField(max_length=300,blank=False,null=False)
	image = models.ImageField(upload_to="img/que/",blank = True)
	answer = models.CharField(max_length=20,blank=False,null=False)
	level = models.IntegerField()
	options = models.CharField(max_length=50,blank=False,null=False)
	hint = models.CharField(max_length=50,blank=False,null=False)
	link = models.URLField(blank=False,null=False)
	points = models.IntegerField()
	
	class Meta:
		unique_together = (("quiz", "level"),)
	
	def __str__(self):
		return self.question
		
class QuizStats(models.Model):
	user = models.ForeignKey(User)
	quiz = models.ForeignKey(Quiz)
	level = models.IntegerField(default=1)
	points = models.IntegerField(default=0)
	lifeline1 = models.BooleanField(default=False)
	lifeline2 = models.BooleanField(default=False)
	lifeline3 = models.BooleanField(default=False)
	level_up_time = models.DateTimeField(null=True,blank=True)
	
	class Meta:
		unique_together = (("user", "quiz"),)
		
	def __str__(self):
		return str(self.quiz.name)+" of "+str(self.user.username)