from django.urls import path
from .views import *

urlpatterns = [
    path('add-job/', add_job, name='add_job'),
    path('job-all/', list_job, name='list_job'),
]