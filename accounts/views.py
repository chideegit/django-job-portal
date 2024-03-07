from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user, update_session_auth_hash
from .form import * 

User = get_user_model()

# Register applicant
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            messages.success(request, 'Your account has been created. Please log in to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register_applicant.html', context)

# Register applicant
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            messages.success(request, 'Your account has been created. Please log in to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register_recruiter.html', context)

# Logs user in. Logged in users must be active and not None (I mean, they shouldn't be)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome to our Site. You are logged in as {user.first_name}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong') # I know! Generic again
            return redirect('login')
    return render(request, 'accounts/login.html')

# Logs out users (Simple terms)
def logout_user(request):
    logout(request)
    messages.success(request, 'Your active session has ended. Log in to continue again')
    return redirect('login') # redirect users to login page after they logout

# Allows users to change their own password, from old to new. 
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # This would allow the user to still stay logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change-password')
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect('password-change')
    else:
        form = UserPasswordChangeForm(request.user)
        context = {'form':form}
    return render(request, 'accounts/change_password.html', context)

# Users can update their profile info
def update_profile(request):
    if request.method == 'POST':
        form = UpdateUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile information has been updated and saved')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('update-profile')
    else:
        form = UpdateUserProfileForm(instance=request.user)
        context = {'form':form}
    return render(request, 'accounts/update_profile.html', context)
