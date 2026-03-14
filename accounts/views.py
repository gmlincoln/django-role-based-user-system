from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CustomUser, RecruiterProfile, JobSeekerProfile 

from jobs.models import Job

from django.contrib.auth import authenticate,login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    jobs = Job.objects.all()
    
    context ={
        'jobs': jobs
    }
    
    return render(request, 'accounts/index.html', context)


def register(request):
    
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_picture')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(username = user_name).exists():
            messages.error(request, 'Username already exist!')
            return redirect('register')
        
        if CustomUser.objects.filter(email = email).exists():
            messages.error(request, 'Email already exist!')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = user_name,
            email = email,
            password = password 
        )
        user.profile_picture = profile_pic
        user.role = role 
     
        user.save()
        
        if role == 'recruiter':
            RecruiterProfile.objects.create(user = user)
        
        elif role == 'job_seeker':
            JobSeekerProfile.objects.create(user = user)
        
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    
    return render(request, 'accounts/register.html')

def login_view(request):
    
    if request.method == 'POST':
        user_input = request.POST.get('email_or_username')
        password = request.POST.get('password')
        
        try:
            user_info = CustomUser.objects.get(email = user_input)
            user_name = user_info.usename 
            
        except CustomUser.DoesNotExist:
            user_name = user_input 
                            
        user = authenticate(request, username = user_name, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credential!')
            return redirect('login')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    
    logout(request)
    messages.success(request, 'Logout Successful')
    
    return redirect('login')

@login_required
def profile(request):
    
    if request.user.role == 'recruiter':
        jobs = Job.objects.filter(recruiter = request.user.recruiterprofile )
    else:
        jobs = Job.objects.none()
        
    context = {
            'jobs':jobs 
        }     
    
    return render(request, 'accounts/profile.html', context)