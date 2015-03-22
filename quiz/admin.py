from django.contrib import admin
from quiz.models import Question,Quiz,QuizStats

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('quiz','level','question','image','answer','hint','link','points')
	list_filter = ('quiz',)
	search_fields = ['quiz__name','question']
	
class QuizAdmin(admin.ModelAdmin):
	list_display = ('name', 'start_time','end_time')
	list_filter = ('start_time','end_time')
	search_fields = ['name']
	
class QuizStatsAdmin(admin.ModelAdmin):
	list_display = ('quiz', 'user','level','points','lifeline1','lifeline2','lifeline3','level_up_time')
	list_filter = ('quiz','user')
	search_fields = ['user__username','user__first_name','user__last_name','quiz__name']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(QuizStats,QuizStatsAdmin)