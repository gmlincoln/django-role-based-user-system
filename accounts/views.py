from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CustomUser, RecruiterProfile, JobSeekerProfile 

# Create your views here.
def home(request):
    
    return render(request, 'accounts/index.html')


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
    
    return render(request, 'accounts/login.html')