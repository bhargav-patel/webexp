from django.contrib import admin
from quiz.models import Question,Quiz,QuizStats

# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizStats)