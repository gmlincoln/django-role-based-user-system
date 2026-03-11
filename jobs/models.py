from django.db import models
from accounts.models import RecruiterProfile

# Create your models here.
class Job(models.Model):
    
    TYPE_CHOICES = (
        ('part_time', 'Part Time'),
        ('full_time', 'Full Time')
    )
    
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    title  = models.CharField(max_length=50)
    description = models.TextField()
    openings = models.IntegerField()
    salary = models.IntegerField()
    job_type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    location = models.CharField(max_length=50)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 