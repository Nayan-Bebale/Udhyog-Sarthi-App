from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import JobForm, CourseForm, LectureForm
from django.forms import inlineformset_factory
from django import forms


from .models import Job, JobSeeker, Contributor, SaveJobs, Courses, Lecture, Blogs, DisabilityType


from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.

# Landing Page

def index(request):

    jobs = Job.objects.all()
    no_marketing = len(Job.objects.filter(job_type='marketing'))
    no_design = len(Job.objects.filter(job_type='design'))
    no_development = len(Job.objects.filter(job_type='development'))
    no_customer = len(Job.objects.filter(job_type='customer'))
    no_health_caare = len(Job.objects.filter(job_type='health_caare'))
    no_automotive = len(Job.objects.filter(job_type='automotive'))
    no_data_entry = len(Job.objects.filter(job_type='data_entry'))
    no_call_center = len(Job.objects.filter(job_type='call_center'))
    context = {
        'jobs': jobs, 
        'no_marketing': no_marketing,
        'no_design': no_design,
        'no_development': no_development,
        'no_customer': no_customer,
        'no_health_caare': no_health_caare,
        'no_automotive': no_automotive,
        'no_data_entry':no_data_entry,
        'no_call_center':no_call_center,
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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user_type = request.POST['type']
        password = request.POST['password']
        
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with this UDID already exists.')
            return redirect('login')  # Replace 'signup' with the name of your sign-up URL

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Perform additional steps based on user type (jobseeker or contributor)
        if user_type == 'jobseeker':
            # Create a jobseeker profile or perform other actions as needed
            JobSeeker.objects.create(user=user)
            return redirect('profile')
        
        elif user_type == 'contributor':
            # Create a contributor profile or perform other actions as needed
            Contributor.objects.create(user=user)
            return redirect('contributor')

        messages.success(request, 'Account created successfully. You can now sign in.')
        return redirect('login')  # Replace 'signin' with the name of your sign-in URL

    else:
        return render(request, 'login.html')  # Replace 'login.html' with the actual path to your login template

def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)

        if user is not None:
            auth_login(request, user)  # Use the imported login function from django.contrib.auth
            messages.success(request, 'Login successful.')

            if JobSeeker.objects.filter(user=user).exists():
                return redirect('profile')
            elif Contributor.objects.filter(user=user).exists():
                return redirect('contributor')
                # Replace 'profile' with the name of your profile view
        else:
            messages.error(request, 'Invalid Name or password.')
            return redirect('login')  # Replace 'signin' with the name of your sign-in URL
    else:
        return render(request, 'login.html')# Replace 'login.html' with the actual path to your login template

def signout(request):
    logout(request)
    return redirect('index')

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

def job_list_by_type(request, job_type):
    jobs = Job.objects.filter(job_type=job_type)

    if job_type == 'marketing':
        job_name = 'Marketing Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 1"
    elif job_type == 'design':
        job_name = 'Design Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 2"
    elif job_type == 'development':
        job_name = 'Development Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 3"
    elif job_type == 'customer':
        job_name = 'Customer Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 4"
    elif job_type == 'health_caare':
        job_name = 'Health and Caare Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 5"
    elif job_type == 'automotive':
        job_name = 'Automotive Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 6"
    elif job_type == 'data_entry':
        job_name = 'Data Entry Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 7"
    elif job_type == 'call_center':
        job_name = 'Call Center Jobs'
        about = "Eirmod sed ipsum dolor sit rebum labore magna erat. Tempor ut dolore lorem kasd vero ipsum sit eirmod sit diam justo sed rebum. 8"
    

    template_name = "type_jobs.html"
    context = {
        'jobs':jobs,
        'job_name':job_name,
        'about':about,
    }
    return render(request, template_name, context)


def blogs(request):
    template_name = "blogs.html"
    return render(request, template_name)


def courses(request):
    template_name = "courses.html"
    return render(request, template_name)

# Staff memmber 

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


# Jobseeker Profile
@login_required(login_url='login')
def profile(request):
    template_name = "profile.html"
    return render(request, template_name)



@login_required(login_url='login')
def edit_jobseeker_profile(request):
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
    template_name = "edit-user-profile.html"
    return render(request, template_name, context)


@login_required(login_url='login')
def contributor(request):
    template_name = "contributor.html"
    return render(request, template_name)


@login_required(login_url='login')
def jobseeker_jobs(request):

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
    template_name = "jobseeker_jobs.html"
    return render(request, template_name, context)


@login_required(login_url='login')
def save_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    user = request.user

    # Check if the job is already saved by the user
    if not SaveJobs.objects.filter(user=user, job=job).exists():
        SaveJobs.objects.create(user=user, job=job)

    return redirect('jobseeker_jobs')



@login_required(login_url='login')
def list_save_job(request):
    save_jobs = SaveJobs.objects.filter(user=request.user).select_related('job')
    
    # Extract the job instances from the queryset
    saved_jobs = [save_job.job for save_job in save_jobs]

    context = {
        'saved': saved_jobs,
    }
    template_name = "saved_jobs.html"
    return render(request, template_name, context)


@login_required(login_url='login')
def delete_save_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    user = request.user

    # Check if the job is already saved by the user
    save_job = SaveJobs.objects.filter(user=user, job=job).first()

    # Check if the save_job exists before attempting to delete
    if save_job:
        save_job.delete()

    return redirect('list_save_job')



@login_required(login_url='login')
def create_course_with_lectures(request):
    CourseFormSet = inlineformset_factory(Courses, Lecture, form=LectureForm, extra=1, can_delete=False)

    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        formset = CourseFormSet(request.POST, instance=Courses())

        if course_form.is_valid() and formset.is_valid():
            course = course_form.save()
            formset.instance = course
            formset.save()

            return redirect('contributor')
    else:
        course_form = CourseForm()
        formset = CourseFormSet(instance=Courses())

    return render(request, 'courses_form.html', {'course_form': course_form, 'formset': formset})


@login_required(login_url='login')
def post_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        abstract = request.POST.get('abstract', '')
        distype_id = request.POST.get('distype')
        content = request.POST.get('content', '')
        thumbnail = request.FILES.get('image')

        if not title or not content:
            messages.error(request, 'Title and Content are required fields.')
            return redirect('post_blog')

        distype = DisabilityType.objects.get(pk=distype_id) if distype_id else None

        blog = Blogs.objects.create(
            user=request.user,
            abstraction=abstract,
            content=content,
            tumbnail=thumbnail,
        )
        print("done nayan")
        blog.save()
        if distype:
            blog.disability_types.add(distype)
            blog.save()

        

        messages.success(request, 'Blog posted successfully.')
        return redirect('post_blog')

    disability_types = DisabilityType.objects.all()
    template_name = "add-blog.html"
    context = {'disability_types': disability_types}
    return render(request, template_name, context)
