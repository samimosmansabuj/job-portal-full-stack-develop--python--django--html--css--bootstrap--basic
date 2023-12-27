from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Recruiter_Profile
from .models import *

# Create your views here.
def add_job(request):
    if request.method == 'POST':
        user = request.user
        if user.user_type != 'Recruiter':
            messages.warning(request, 'Only Recruiter are allowed to add job!')
            return redirect('profile', username=user.username)
        
        recruiter = Recruiter_Profile.objects.get(user=user)
        job_title = request.POST['job_title']
        job_details = request.POST['job_details']
        vacancy = request.POST['vacancy']
        salary = request.POST['salary']
        employment_status = request.POST['employment_status']
        gender_allow = request.POST['gender_allow']
        application_deadline = request.POST['application_deadline']
        
        job = Job.objects.create(
            recruiter = recruiter,
            job_title = job_title,
            job_details = job_details,
            vacancy = vacancy,
            salary = salary,
            employment_status = employment_status,
            gender_allow = gender_allow,
            application_deadline = application_deadline,
        )
        messages.success(request, 'Add a New Job Successfull!')
        return redirect('profile', username=user.username)
        
    return render(request, 'job/add_job.html')


def list_job(request):
    job = Job.objects.all()
    context = {'job': job}
    return render(request, 'job/job_list.html', context)


