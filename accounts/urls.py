from django.urls import path
from django.contrib.auth import views as auth_views
from .views import * 

urlpatterns = [
    path('register-applicant/', register_applicant, name='register-applicant'),
    path('register-recruiter', register_recruiter, name='register-recruiter'),    
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('change-password/', change_password, name='change-password'), 
    path('update-profile/', update_profile, name='update-profile'),

    # reset password links (default from django)
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name = "accounts/reset_password.html"), name ='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name ='password_reset_complete'),
]