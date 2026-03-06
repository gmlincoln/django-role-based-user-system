from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter')
    )
    
    profile_picture = models.ImageField(upload_to='profile/', null = True, blank = True)
    role = models.CharField(max_length = 30, choices = ROLE_CHOICES)
    
    
class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Recruiter {self.user.username}"
    
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.CharField(max_length=30)
    bio = models.TextField()
    
    def __str__(self):
        return f"Seeker {self.user.username}"