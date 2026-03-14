from django.urls import path
from . import views 
urlpatterns = [
    path('create_job', views.create_job, name='create_job'),
    path('delete_job/<int:job_id>', views.delete_job, name='delete_job'),
    path('update_job/<int:job_id>', views.update_job, name='update_job'),
    path('job_details/<int:job_id>', views.job_details, name="job_details"),
    
]