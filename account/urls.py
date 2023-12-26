from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('sign-in/', signin, name='signin'),
    path('logout/', Logout, name='logout'),
    path('forget-password/', forget_password, name='forget_password'),
    path('forget-password-reset/', forget_password_reset, name='forget_password_reset'),
    
    path('profile/<username>/', profile, name='profile'),
    path('recruiter-job/<username>/', recruiter_job_list, name='recruiter_job_list'),
    path('jobseeker/update/', jobseeker_profile_update, name='jobseeker_profile_update'),
    path('recruiter/update/', recruiter_profile_update, name='recruiter_profile_update'),
]