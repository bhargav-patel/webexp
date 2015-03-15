from django.contrib import admin
from quiz.models import Question
from authentication.models import Profile

# Register your models here.

admin.site.register(Question)
admin.site.register(Profile)