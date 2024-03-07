from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model, because why not?"""
    email = models.EmailField(unique=True, null=False, blank=False)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)