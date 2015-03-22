from django.contrib import admin
from authentication.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','college','enroll_no','mobile')
	list_filter = ('college',)
	search_fields = ['user__username','user__first_name','user__last_name','college','mobile','enroll_no']

admin.site.register(Profile,ProfileAdmin)