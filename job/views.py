from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .form import * 
from company.models import Company
from django_project.decorator import no_company_no_job

@login_required
@no_company_no_job
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            company = Company.objects.get(user=request.user)
            var.company = company
            var.user = request.user
            var.save()
            messages.success(request, 'New job added. Applicants can now see your job ad and apply to it')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('dashboard')
    else:
        form = AddJobForm()
        context = {'form':form}
    return render(request, 'job/add_job.html', context )

@login_required
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form information has been updated and saved')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('dashboard')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form':form}
    return render(request, 'job/update_job.html', context)

@login_required
def jobs_per_company(request, pk):
    company = Company.objects.get(pk=pk)
    jobs = company.job_set.all()
    context = {'jobs':jobs}
    return render(request, 'job/jobs_per_company.html', context)


