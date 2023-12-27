from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404
from notifications.signals import notify
from django.contrib import messages
from .forms import Job_Form
from account.models import *
from .models import *

# Create your views here.
def add_job(request):
    form = Job_Form()
    
    if request.method == 'POST':
        user = request.user
        if user.user_type != 'Recruiter':
            messages.warning(request, 'Only Recruiter are allowed to add job!')
            return redirect('profile', username=user.username)
        
        recruiter = Recruiter_Profile.objects.get(user=user)
        
        data = Job_Form(request.POST)
        if data.is_valid():
            job = data.save()
            job.recruiter = recruiter
            job.save()
            messages.success(request, 'Add a New Job Successfull!')
            
            job_seeker = Custom_User.objects.filter(user_type='JobSeeker')
            notify.send(user, recipient=job_seeker, verb="Add New Job")
            
            return redirect('profile', username=user.username)
        
    return render(request, 'job/add_job.html', {'form': form})



def update_job(request, slug):
    job = Job.objects.get(slug=slug)
    form = Job_Form(instance=job)
    context = {'job': job, 'form': form}
    
    if request.method == 'POST':
        user = request.user
        if user.user_type != 'Recruiter':
            messages.warning(request, 'Only Recruiter are allowed to add job!')
            return redirect('profile', username=user.username)

        recruiter = Recruiter_Profile.objects.get(user=user)
        if job.recruiter != recruiter:
            messages.warning(request, 'You are not authorize for update this job!')
            return redirect('profile', username=user.username)
    
        data = Job_Form(request.POST, instance=job)
        if data.is_valid():
            data.save()
            messages.success(request, 'Update Job Successfull!')
            return redirect('profile', username=user.username)
        
    return render(request, 'job/add_job.html', context)


def list_job(request):
    job = Job.objects.all()
    user_save_job_id_list = Saved_Job.objects.filter(user=request.user).values_list('job__id', flat=True)
    context = {'job': job, 'user_save_job_id_list': user_save_job_id_list}
    return render(request, 'job/job_list/job_list.html', context)


def job_view(request, slug):
    job = Job.objects.get(slug=slug)
    context = {'job': job}
    return render(request, 'job/job_view.html', context)


def job_apply(request, id):
    if request.user.user_type != 'JobSeeker':
        return redirect('profile', username=user.username)
    
    job = Job.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        apply_skills = request.POST['apply_skills']
        apply_cv = request.FILES.get('apply_cv')
        
        application = Job_Apply.objects.create(
            User=user,
            job=job,
            skills=apply_skills,
            apply_resume_cv=apply_cv,
        )
        application.save()
        messages.success(request, 'Application Apply Successfully!')
        return redirect('profile', username=user.username)
    
    return render(request, 'job/job_apply.html', {'job': job})

