from django.contrib import admin
from .models import *

# Register your models here.
class Job_Admin(admin.ModelAdmin):
    list_display = ['job_title', 'vacancy', 'employment_status', 'application_deadline']

admin.site.register(Job, Job_Admin)
admin.site.register(Job_Apply)
admin.site.register(Saved_Job)
