from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.forms import inlineformset_factory
from django import forms

from contributor.forms import CourseForm, LectureForm
from .models import Job, JobSeeker, Contributor, SaveJobs, Courses, Lecture, Blogs, DisabilityType
from django.db.models.functions import TruncMonth
from django.db.models import Count


from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['_', '@']
# Create your views here.

#################################### Landing Page System ####################################



def index(request):
    print(request.user)
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


# Login and Signup System starts ###############################

def login(request):
    template_name = "login.html"
    return render(request, template_name)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user_type = request.POST['type']
        password = request.POST['password']
        password2 = request.POST['password2']

        
        # Check if the username contains '@' or '_'
        if not any(char in symbols for char in username):
            messages.error(request, "Username must contain '@' or '_'")
            return redirect('login')

        # Check if the user already exists
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'A user with this username already exists.')
            return redirect('login')  # Replace 'signup' with the name of your sign-up URL

        # Check if passwords match
        elif password != password2:
            messages.error(request, "Passwords do not match. Please recheck.")
            return redirect('login')


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
        elif user_type == 'parent':
            # Create a parent profile or perform other actions as needed
            
            return redirect('index')

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
                return redirect('profile', user_id=user.id)
            elif Contributor.objects.filter(user=user).exists():
                return redirect('contributor', user_id=user.id)
                # Replace 'profile' with the name of your profile view
        else:
            messages.error(request, 'Invalid Name or password.')
            return redirect('usa:login')  # Replace 'signin' with the name of your sign-in URL
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

def main_dis_type(request, name):
    blogs = DisabilityType.objects.filter(name=name)

    template_name = "disable-blogs.html"
    context = {
        'blogs':blogs,
    }
    return render(request, template_name, context)


################################# LANDING PAGE BLOGs
def blogs(request):
    context = {
        "blogs":Blogs.objects.all(),
        "blogs_archive": Blogs.objects.annotate(month=TruncMonth('created_at')).values('month').distinct(),
    }
    template_name = "blogsSystem/blogs.html"
    return render(request, template_name, context)

def blog_post_detail_page(request, blogid):
    obj = get_object_or_404(Blogs, id_blog=blogid)
    print(obj)
    context = {"object":obj}
    template_name = "blogsSystem/blog_details.html"
    return render(request, template_name, context)



def blog_by_type(request, categories):
    blogs = DisabilityType.objects.filter(categories=categories)

    if categories == 'a':
        title = 'Categories:A Blindness and low vision'
    elif categories == 'b':
        title = 'Categories:B Deaf and Hard of Hearing'
    elif categories == 'c':
        title = 'Categories:C Locomotor disabilities'
    elif categories == 'd':
        title = 'Categories:D Autism, intellectual disability, specific learning disability, and mental illness'
    elif categories == 'e':
        title = 'Categories:E Multiple disabilities'

    template_name = "specific_type.html"
    context = {
        'blogs':blogs,
        'title': title,
    }
    return render(request, template_name, context)

def blog_month(request, year, month):
    date = f"{year}-{month}"
    blogs = Blogs.objects.filter(created_at__year=year, created_at__month=month)
    print(blogs)
    context = {
        "blogs": blogs,
        "month_name": date,  # For displaying the month name in the template
    }
    template_name = "blogsSystem/blog_month.html"  # Assuming a separate template for monthly view
    return render(request, template_name, context)


def courses(request):
    course = Courses.objects.all()

    context = {
        'course':course,
    }
    template_name = "courses.html"
    return render(request, template_name, context)


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


def main_dis_type(request, name):
    blogs = DisabilityType.objects.filter(name=name)

    template_name = "disable-blogs.html"
    context = {
        'blogs':blogs,
    }
    return render(request, template_name, context)

