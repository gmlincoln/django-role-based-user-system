from django.shortcuts import get_object_or_404, redirect, render
from .models import Job

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

@login_required
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


@login_required
def update_job(request, job_id):
    job = Job.objects.get(id = job_id, recruiter = request.user.recruiterprofile )
    
    
    if request.method == "POST":
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.openings = request.POST.get('openings')
        job.job_type = request.POST.get('job_type')
        job.location = request.POST.get('location')
        job.deadline = request.POST.get('deadline')
        job.salary = request.POST.get('salary')
        
        job.save()
        messages.success(request, "Job Successfully Updated!")
        
        return redirect('profile') 
    
    context = {
        'job': job
    }
    
    return render(request, 'jobs/update_job.html', context)


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id = job_id, recruiter = request.user.recruiterprofile)

    job.delete()
    messages.success(request, "Job delete Successfully!")
    
    return redirect('profile')

def job_details(request, job_id):
    
    job = get_object_or_404(Job, id = job_id)
    
    context = {
        'job' : job,
        
    }
    
    return render(request, 'jobs/job_details.html', context)
    