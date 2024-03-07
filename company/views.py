from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .form import * 
from .models import * 
from django_project.decorator import check_company

User = get_user_model()

@check_company
def add_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user 
            user = User.objects.get(id=request.user.id)
            user.has_company = True 
            user.save()
            var.save()
            messages.success(request, f'Your company {var.name} has been added and saved to DB')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('add-company')
    else:
        form = AddCompanyForm()
        context = {'form':form}
    return render(request, 'company/add_company.html', context)

@user_passes_test
def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company information is being updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('dashboard')
    else:
        form = UpdateCompanyForm(instance=company)
        context = {'form':form}
    return render(request, 'company/update_company.html', context)

def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'company/company_details.html', context)