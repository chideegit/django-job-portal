from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company

User = get_user_model()

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    job_location = models.CharField(
        max_length=50, 
        choices = (('Remote', 'Remote'), ('Onsite', 'Onsite'), ('Hybrid', 'Hybrid'))
    )
    job_type = models.CharField(
        max_length=20, 
        choices = (('Full Time', 'Full Time'), ('Part Time', 'Part Time'))
    )
    end_date = models.DateField()
    posted_on = models.DateTimeField(auto_now_add=True)

