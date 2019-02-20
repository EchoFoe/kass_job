from django.contrib import admin
from .models import *


class Job_seekerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Job_seeker._meta.fields]
    list_filter = ['email', 'job_seeker_phone', 'job_seeker_specialty']
    search_fields = ['email', 'job_seeker_phone', 'last_name']

    class Meta:
        model = Job_seeker


admin.site.register(Job_seeker, Job_seekerAdmin)
