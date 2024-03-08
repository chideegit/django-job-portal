from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()

def check_company(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if user.has_company:
            messages.warning(request, 'Permission Denied. Seems you already have a company')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper

def no_company_no_job(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.has_company:
            messages.warning(request, 'Permission Denied. You must add a company before posting jobs')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper