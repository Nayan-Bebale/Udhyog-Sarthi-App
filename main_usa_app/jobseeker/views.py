from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.forms import inlineformset_factory
from .forms import JobApplicationForm
from django import forms

from usa.models import Job, JobSeeker, SaveJobs, Applicant, Blogs
from django.db.models.functions import TruncMonth

from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse



####################################### Jobseeker Profile ###################

def profile(request, user_id):
    if request.user.is_authenticated and JobSeeker.objects.filter(user=request.user).exists():
        published_jobs = Job.objects.filter(is_published=True).order_by('-updated_at')
        jobs = published_jobs.filter(is_closed=False)

        applied_jobs = []
        for job in jobs:
            if Applicant.objects.filter(user=request.user, job=job).exists():
                applied_jobs.append(job.job_id)

        # Check Already Appled or not
        
        context = {
            'jobs':jobs,
            'applied_jobs': applied_jobs,
            'blogs': Blogs.objects.all(),
        }
        template_name = "jobseekers/profile.html"
        return render(request, template_name, context)
    else:
        return redirect('index')


@login_required(login_url='login')
def user_profile(request, user_id):
    user_profile = JobSeeker.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    template_name = "jobseekers/user_profile.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def edit_jobseeker_profile(request, user_id):
    user_profile = JobSeeker.objects.get(user=request.user)

    if request.method == 'POST':
        image = request.FILES.get('image', user_profile.profileimg)
        username = request.POST.get('username', user_profile.username)
        bio = request.POST.get('bio', user_profile.bio)
        about = request.POST.get('about', user_profile.about)
        distype = request.POST.get('distype', user_profile.dis_type)
        udid = request.POST.get('udid', user_profile.udid)
        dob = request.POST.get('dob', user_profile.dob)
        phone = request.POST.get('phone', user_profile.phone_number)
        location = request.POST.get('location', user_profile.location)
        city = request.POST.get('city', user_profile.city)

        user_profile.username = username
        user_profile.bio = bio
        user_profile.profileimg = image
        user_profile.about = about
        user_profile.dis_type = distype
        user_profile.udid = udid
        user_profile.dob = dob
        user_profile.phone_number = phone
        user_profile.location = location
        user_profile.city = city
        user_profile.save()

        return redirect('edit_jobseeker_profile')

    context = {
        'user_profile': user_profile,
    }
    template_name = "jobseekers/edit_jobseeker_profile.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def jobseeker_jobs(request, user_id):

    jobs = Job.objects.all()
    no_marketing = Job.objects.filter(job_type='marketing')
    no_design = Job.objects.filter(job_type='design')
    no_development = Job.objects.filter(job_type='development')
    no_customer = Job.objects.filter(job_type='customer')
    no_health_caare = Job.objects.filter(job_type='health_caare')
    no_automotive = Job.objects.filter(job_type='automotive')
    no_data_entry = Job.objects.filter(job_type='data_entry')
    no_call_center = Job.objects.filter(job_type='call_center')
    context = {
        'jobs': jobs, 
        'marketing': no_marketing,
        'design': no_design,
        'development': no_development,
        'customer': no_customer,
        'health_caare': no_health_caare,
        'automotive': no_automotive,
        'data_entry':no_data_entry,
        'call_center':no_call_center,
    }
    template_name = "jobseekers/jobseeker_jobs.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def save_job(request, job_id, user_id):
    job = Job.objects.get(pk=job_id)
    user = request.user

    # Check if the job is already saved by the user
    if not SaveJobs.objects.filter(user=user, job=job).exists():
        SaveJobs.objects.create(user=user, job=job)

    return redirect('jobseeker_jobs', user_id=user.id)

@login_required(login_url='login')
def list_save_job(request, user_id):
    save_jobs = SaveJobs.objects.filter(user=request.user).select_related('job')
    
    # Extract the job instances from the queryset
    saved_jobs = [save_job.job for save_job in save_jobs]

    # Check Already Appled or not
    applied_jobs = []
    for job in saved_jobs:
        if Applicant.objects.filter(user=request.user, job=job).exists():
            applied_jobs.append(job.job_id)

    context = {
        'saved': saved_jobs,
        'applied_jobs': applied_jobs,
    }
    template_name = "jobseekers/saved_jobs.html"
    return render(request, template_name, context)


@login_required(login_url='login')
def delete_save_job(request, job_id, user_id):
    job = get_object_or_404(Job, pk=job_id)
    user = request.user

    # Check if the job is already saved by the user
    save_job = SaveJobs.objects.filter(user=user, job=job).first()

    # Check if the save_job exists before attempting to delete
    if save_job:
        save_job.delete()

    return redirect('list_save_job', user_id=user.id)

@login_required(login_url='login')
def show_details_jobs(request, job_id, user_id):
    job = get_object_or_404(Job, pk=job_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the user has already applied for this job
            if Applicant.objects.filter(user=request.user, job=job).exists():
                messages.error(request, "You have already applied for this job.")
                return redirect('show_details_jobs', job_id=job_id)
            
            # If not, save the application
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.job = job
            applicant.save()
            return redirect('show_details_jobs', job_id=job_id)
    else:
        form = JobApplicationForm()

    context = {
        'job': job,
        'form': form,
    }
    template_name = 'jobseekers/applied_job.html'
    return render(request, template_name, context)


@login_required(login_url='login')
def blogs_jobseekers(request, user_id):
    context = {
        "blogs":Blogs.objects.all(),
        "blogs_archive": Blogs.objects.annotate(month=TruncMonth('created_at')).values('month').distinct(),
    }
    template_name = "jobseekers/blogSystem/blogs.html"
    return render(request, template_name, context)


@login_required(login_url='login')
def blog_details_jobseeker(request, blogid, user_id):
    obj = get_object_or_404(Blogs, id_blog=blogid)
    context = {"object":obj}
    template_name = "jobseekers/blogSystem/blog_details.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def blog_by_month(request, year, month, user_id):
    date = f"{year}-{month}"
    blogs = Blogs.objects.filter(created_at__year=year, created_at__month=month)
    context = {
        "blogs": blogs,
        "month_name": date,  # For displaying the month name in the template
    }
    template_name = "jobseekers/blogSystem/blog_months.html"  # Assuming a separate template for monthly view
    return render(request, template_name, context)

    