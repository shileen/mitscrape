from django.contrib import admin
from scrape.models import Attendance, Gpalist, UserProfile
# Register your models here.


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'attended', 'absent']
    list_filter = ['user']
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Gpalist)
admin.site.register(UserProfile)
