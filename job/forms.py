from django import forms
from .models import Job

class Job_Form(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'job_details', 'vacancy', 'salary', 'employment_status', 'gender_allow', 'application_deadline']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'job_details': forms.Textarea(attrs={'class': 'form-control'}),
            'vacancy': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'employment_status': forms.Select(attrs={'class': 'form-control'}),
            'gender_allow': forms.Select(attrs={'class': 'form-control'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Example: 2000-10-30'}),
        }