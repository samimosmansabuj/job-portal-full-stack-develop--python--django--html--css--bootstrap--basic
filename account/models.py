from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Recruiter', 'Recruiter'),
        ('JobSeeker', 'JobSeeker'),
        ('Employee', 'Employee'),
        ('Admin', 'Admin'),
    )
    display_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    user_type = models.CharField(choices=USER_TYPE, max_length=50, blank=True, null=True)
    
    auth_token = models.CharField(max_length=500, blank=True, null=True)
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.display_name

class Recruiter_Profile(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_phone_number = models.CharField(max_length=14, blank=True, null=True)
    company_email = models.EmailField(max_length=200, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='company/logo/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.company_name

class JobSeeker_Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='jobseeker/', blank=True, null=True)
    cv = models.FileField(upload_to='jobseeker/cv/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    
