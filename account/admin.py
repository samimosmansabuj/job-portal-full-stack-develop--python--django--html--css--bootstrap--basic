from django.contrib import admin
from .models import *

# Register your models here.
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'user_type', 'is_verified']

class Recruiter_Profile_Admin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'company_phone_number', 'company_email']

class JobSeeker_Profile_Admin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth']


admin.site.register(Custom_User, Custom_User_Admin)
admin.site.register(Recruiter_Profile, Recruiter_Profile_Admin)
admin.site.register(JobSeeker_Profile, JobSeeker_Profile_Admin)



