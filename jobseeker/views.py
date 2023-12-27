from django.shortcuts import render, redirect, HttpResponse
from job.models import Job, Saved_Job
from django.contrib import messages

# Create your views here.
def add_saved_job(request, id):
    job = Job.objects.get(id=id)
    user = request.user
    user_saved_job = Saved_Job.objects.filter(user=user)
    user_save_job_id_list = Saved_Job.objects.filter(user=user).values_list('job__id', flat=True)
    
    print(user_save_job_id_list)
    
    if user.user_type == 'JobSeeker':
        for user_saved_job in user_saved_job:
            if job == user_saved_job.job:
                user_saved_job.delete()
                messages.success(request, 'Job Saved Removed!')
                return redirect(request.META['HTTP_REFERER'])
        
        saved_job = Saved_Job.objects.create(
            user = user,
            job = job,
        )
        saved_job.save()
        messages.success(request, 'Job Saved Added!')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.warning(request, 'Only JobSeeker Saved the Job!')
        return redirect(request.META['HTTP_REFERER'])
