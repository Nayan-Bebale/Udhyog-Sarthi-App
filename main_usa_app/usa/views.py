from django.shortcuts import render, redirect
from .forms import JobForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Job

# Create your views here.

def index(request):

    jobs = Job.objects.all()
    
    context = {
        'jobs': jobs, 
    }
    template_name = "index.html"
    return render(request, template_name, context)

def contect(request):
    template_name = "contact.html"
    return render(request, template_name)

def about(request):
    template_name = "about.html"
    return render(request, template_name)

def login(request):
    template_name = "login.html"
    return render(request, template_name)

def property_list(request):
    part_time_jobs = Job.objects.filter(time='part_time')
    full_time_jobs = Job.objects.filter(time='full_time')
    intern_jobs = Job.objects.filter(time='internship')


    context = {
        'part_time_jobs': part_time_jobs,
        'full_time_jobs':full_time_jobs,
        'intern_jobs':intern_jobs,
    }
    template_name = "property-list.html"
    return render(request, template_name, context)

def property_agent(request):
    template_name = "property-agent.html"
    return render(request, template_name)

def property_type(request):
    template_name = "property-type.html"
    return render(request, template_name)

def testimonial(request):
    template_name = "testimonial.html"
    return render(request, template_name)


@staff_member_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the posted_by field to the current staff member
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('post_job')  # Redirect to the job list page
    else:
        form = JobForm()

    return render(request, 'post_job.html', {'form': form})