from django.db import models
from account.models import *
from django.utils.text import slugify

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
    recruiter = models.ForeignKey(Recruiter_Profile, on_delete=models.CASCADE, blank=True, null=True)
    
    job_title = models.CharField(max_length=900)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    job_details = models.TextField(blank=True, null=True)
    vacancy = models.CharField(blank=True, null=True, default='Not specific', max_length=50)
    salary = models.PositiveIntegerField(blank=True, null=True)
    employment_status = models.CharField(choices=EMPLOYMENT_STATUS, blank=True, null=True, max_length=50)
    gender_allow = models.CharField(choices=GENDER_ALLOW, blank=True, null=True, max_length=50)
    application_deadline = models.DateField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        return super(Job, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.job_title



class Job_Apply(models.Model):
    STATUS = (
        ('Applied', 'Applied'),
        ('Company View', 'Company View'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
        ('Awaiting', 'Awaiting'),
    )
    User = models.ForeignKey(Custom_User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.CharField(max_length=100, blank=True, null=True)
    apply_resume_cv = models.FileField(upload_to='apply_job/cv/', blank=True, null=True)
    status = models.CharField(choices=STATUS, default='Applied', blank=True, null=True, max_length=50)
    
    def __str__(self) -> str:
        return self.User.username+' Application For '+self.job.job_title


