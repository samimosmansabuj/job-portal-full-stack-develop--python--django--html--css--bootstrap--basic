from django.urls import path
from .views import *

urlpatterns = [
    path('saved_job/<int:id>/', add_saved_job, name='add_saved_job')
]