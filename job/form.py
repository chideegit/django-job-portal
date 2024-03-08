from django import forms 
from .models import Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'user', 'posted_on')

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'user', 'posted_on')