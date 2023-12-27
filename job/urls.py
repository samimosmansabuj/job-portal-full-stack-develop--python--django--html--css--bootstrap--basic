from django.urls import path
from .views import *

urlpatterns = [
    path('add-job/', add_job, name='add_job'),
    path('update-job/<slug>/', update_job, name='update_job'),
    path('job-all/', list_job, name='list_job'),
    path('job-apply/<int:id>/', job_apply, name='job_apply'),
]