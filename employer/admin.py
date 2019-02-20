from django.contrib import admin
from .models import *


class EmployerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employer._meta.fields]
    list_filter = ['email', 'employer_phone']
    search_fields = ['email', 'employer_phone', 'last_name']

    class Meta:
        model = Employer


admin.site.register(Employer, EmployerAdmin)
