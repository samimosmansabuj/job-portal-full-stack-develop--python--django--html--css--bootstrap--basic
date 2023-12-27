from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.conf import settings
from job.models import *
from .models import *
from django.contrib import messages
import random
import os

# Create your views here.
def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        context = {'email': email}
        user = Custom_User.objects.get(email=email)
        otp = random.randint(111111, 999999)
        
        user.otp_token = otp
        user.save()
        
        #For Environment For Send Mail---------
        subject = "Verification For Forget Password!"
        message = f"""Dear {user.display_name}
        Your OTP is {otp}"""
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
        #For Environment For Send Mail---------
        
        return render(request, 'account/forget_password_reset.html', context)
    return render(request, 'account/forget_password.html')

def forget_password_reset(request):
    if request.method =='POST':
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        
        user = Custom_User.objects.get(email=email)
        if user.otp_token != otp:
            messages.warning(request, "OTP Does not match!")
            return redirect(request.META['HTTP_REFERER'])

        user.set_password(password)
        user.otp_token = None
        user.save()
        messages.success(request, "Password Reset Successfull!")
        return redirect('signin')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        display_name = request.POST.get('display_name')
        phone_number = request.POST.get('phone_number')
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Custom_User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            display_name=display_name,
            phone_number=phone_number,
            user_type=user_type,
            email=email,
            password=password,
        )
        if user_type == 'Recruiter':
            recruiter = Recruiter_Profile.objects.create(user=user, company_phone_number=phone_number, company_email=email)
        elif user_type == 'JobSeeker':
            jobseeker = JobSeeker_Profile.objects.create(user=user)
        
        return redirect('signin')
    return render(request, 'account/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'account/signin.html')

def Logout(request):
    logout(request)
    return redirect('signin')




def profile(request, username):
    user = Custom_User.objects.get(username=username)
    if user.user_type == 'JobSeeker':
        jobseeker = JobSeeker_Profile.objects.get(user=user)
        context = {'user': user, 'jobseeker': jobseeker}
        return render(request, 'account/jobseeker_profile/profile.html', context)
    
    elif user.user_type == 'Recruiter':
        recruiter = Recruiter_Profile.objects.get(user=user)
        context = {'user': user, 'recruiter': recruiter}
        return render(request, 'account/recruiter_profile/profile.html', context)
    
    else:
        return HttpResponse('Wrong Credential')

def jobseeker_profile_update(request):
    if request.user.user_type != 'JobSeeker':
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        display_name = request.POST['display_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        user = Custom_User.objects.get(username=username)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.display_name=display_name
        user.email=email
        user.phone_number=phone_number
        user.save()
        
        date_of_birth = request.POST.get('birthday')
        gender = request.POST.get('gender')
        profile_picture = request.FILES.get('profile_picture')
        cv = request.FILES.get('cv')
        
        jobseeker = JobSeeker_Profile.objects.get(user=user)
        if date_of_birth:
            jobseeker.date_of_birth = date_of_birth
        if gender:
            jobseeker.gender = gender
        if cv:
            if jobseeker.cv:
                os.remove(jobseeker.cv.path)
            jobseeker.cv = cv
        
        if profile_picture:
            if jobseeker.profile_picture:
                os.remove(jobseeker.profile_picture.path)
            jobseeker.profile_picture = profile_picture
        
        jobseeker.save()
        
        messages.success(request, 'Update Sucessfull!')
        return redirect(request.META['HTTP_REFERER'])

def applied_job(request, username):
    user = Custom_User.objects.get(username=username)
    job_application = Job_Apply.objects.filter(User=user)
    return render(request, 'account/jobseeker_profile/applied_job.html', {'job_application': job_application})

def saved_job(request, username):
    user = Custom_User.objects.get(username=username)
    saved_job = Saved_Job.objects.filter(user=user)
    context = {'saved_job': saved_job}
    saved_job_list = []
    for saved_job in saved_job:
        saved_job_list.append(saved_job.job)
    context['saved_job_list'] = saved_job_list
    return render(request, 'account/jobseeker_profile/saved_job.html', context)

def notification(request, username):
    user = Custom_User.objects.get(username=username)
    if user.user_type == 'JobSeeker':
        return render(request, 'account/jobseeker_profile/notification.html')
    elif user.user_type == 'Recruiter':
        return render(request, 'account/recruiter_profile/notification.html')
    


def recruiter_profile_update(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        display_name = request.POST['display_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        user = Custom_User.objects.get(username=username)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.display_name=display_name
        user.email=email
        user.phone_number=phone_number
        user.save()
        
        recruiter = Recruiter_Profile.objects.get(user=user)
        
        recruiter.company_name = request.POST.get('company_name')
        recruiter.company_phone_number = request.POST.get('company_phone_number')
        recruiter.company_email = request.POST.get('company_email')
        recruiter.company_address = request.POST.get('company_address')
        if request.FILES.get('company_logo'):
            if recruiter.company_logo:
                os.remove(recruiter.company_logo.path)
            recruiter.company_logo = request.FILES.get('company_logo')
        
        recruiter.save()
        messages.success(request, 'Update Sucessfull!')
        return redirect(request.META['HTTP_REFERER'])

def recruiter_job_list(request, username):
    user = Custom_User.objects.get(username=username)
    recruiter = Recruiter_Profile.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    context = {'job': job}
    return render(request, 'account/recruiter_profile/recruiter_job.html', context)
        

