from django.contrib import admin
from .models import CustomUser, RecruiterProfile, JobSeekerProfile

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)