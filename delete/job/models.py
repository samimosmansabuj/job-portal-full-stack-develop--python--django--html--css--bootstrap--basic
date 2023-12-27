from django.db import models
from account.models import Recruiter_Profile

# Create your models here.
class Job(models.Model):
    EMPLOYMENT_STATUS = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Remote', 'Remote'),
    )
    GENDER_ALLOW = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Both', 'Both'),
    )
    recruiter = models.ForeignKey(Recruiter_Profile, on_delete=models.CASCADE)
    
    job_title = models.CharField(max_length=900)
    job_details = models.TextField(blank=True, null=True)
    vacancy = models.CharField(blank=True, null=True, default='Not specific', max_length=50)
    salary = models.PositiveIntegerField(blank=True, null=True)
    employment_status = models.CharField(choices=EMPLOYMENT_STATUS, blank=True, null=True, max_length=50)
    gender_allow = models.CharField(choices=GENDER_ALLOW, blank=True, null=True, max_length=50)
    application_deadline = models.DateField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.job_title
    
