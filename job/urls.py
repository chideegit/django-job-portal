from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-job', add_job, name='add-job'), 
    path('update-job/<int:pk>/', update_job, name='update-job'), 
    path('jobs-per-company/<int:pk>/', jobs_per_company, name='jobs-per-company'),
    path('delete-job/<int:pk>/', delete_job, name='delete-job')
]