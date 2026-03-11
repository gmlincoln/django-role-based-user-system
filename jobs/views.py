from django.shortcuts import redirect, render
from .models import Job

from django.contrib import messages

# Create your views here.

def create_job(request):
    if request.method == "POST":
        job_title = request.POST.get('title')
        job_description = request.POST.get('description')
        vacancy = request.POST.get('openings')
        job_type = request.POST.get('job_type')
        job_location = request.POST.get('location')
        application_deadline = request.POST.get('deadline')
        salary = request.POST.get('salary')
        
        recruiter_profile = request.user.recruiterprofile 
        
        Job.objects.create(
            recruiter = recruiter_profile,
            title = job_title,
            description = job_description,
            openings = vacancy,
            salary = salary,
            job_type = job_type,
            location = job_location,
            deadline = application_deadline
        )
        messages.success(request, 'Job Created Successfully!')
        return redirect('profile')        
        
    return render(request, 'jobs/create_job.html')