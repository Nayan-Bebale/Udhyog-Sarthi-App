from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import JobForm, CompanyForm
from django.forms import inlineformset_factory
from django import forms


from usa.models import Job, Contributor,Companies, Blogs, DisabilityType, Applicant

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.db.models import Count




# Create your views here.

@login_required(login_url='login')
def contributor(request, user_id):
    if request.user.is_authenticated and Contributor.objects.filter(user=request.user).exists():
        published_jobs = Job.objects.filter(is_published=True).order_by('-updated_at')
        jobs = published_jobs.filter(is_closed=False)
        context = {
            "jobs":jobs,
            }
        template_name = "contributors/contributor.html"
        return render(request, template_name, context)
    else:
        return redirect('index')

@login_required(login_url='login')
def edit_contributor_profile(request, user_id):
    user_profile = Contributor.objects.get(user=request.user)

    if request.method == 'POST':
        image = request.FILES.get('image', user_profile.profileimg)
        username = request.POST.get('username', user_profile.user)
        bio = request.POST.get('bio', user_profile.bio)
        

        user_profile.user = username
        user_profile.bio = bio
        user_profile.profileimg = image
        user_profile.save()

        return redirect('edit_contributor_profile')

    context = {
        'user_profile': user_profile,
    }
    template_name = "contributors/edit-contributor-profile.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def blog_post_list_view(request, user_id):
    obj = Blogs.objects.filter(user=request.user)
    context = {"object": obj}
    template_name = "contributors/blog_post_list.html"
    return render(request, template_name, context)

@login_required(login_url='login')
def post_blog(request, user_id):
    if request.method == 'POST':
        title = request.POST['title']
        abstract = request.POST.get('abstract', '')
        distype_id = request.POST.get('distype')
        categories = request.POST.get('categories')
        content = request.POST.getlist('content')[0] if request.POST.getlist('content') else ''
        thumbnail = request.FILES.get('image')

        if not title or not content:
            messages.error(request, 'Title and Content are required fields.')
            return redirect('post_blog')

        distype = DisabilityType.objects.get(pk=distype_id) if distype_id else None

        blog = Blogs.objects.create(
            user=request.user,
            abstraction=abstract,
            categories=categories,
            content=content,
            tumbnail=thumbnail,
        )
        blog.save()
        if distype:
            blog.disability_types.add(distype)
            blog.save()

        

        messages.success(request, 'Blog posted successfully.')
        return redirect('post_blog')

    disability_types = DisabilityType.objects.all()
    template_name = "contributors/add-blog.html"
    context = {'disability_types': disability_types, 'categories_choices': Blogs.categories_choices}
    return render(request, template_name, context)

def blog_post_update_view(request, blogid, user_id):
    obj = get_object_or_404(Blogs, id_blog=blogid)
    template_name = "blog_post_update.html"
    context = {"object":obj, "form":None}
    return render(request, template_name, context)

def blog_post_delete_view(request, blogid, user_id):
    obj = get_object_or_404(Blogs, id_blog=blogid)
    template_name = "blog_post_delete.html"
    context = {"object":obj}
    return render(request, template_name, context)



####################### Job System ##################


@login_required
def post_job(request, user_id):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Get the selected disability types
            distypes = form.cleaned_data['distypes']
            company = Companies.objects.filter(user=request.user).first()
            if not company:
                # Redirect to add_company view if the user doesn't have a company profile
                return redirect('add_company')
            # Create a new Job instance
            new_job = form.save(commit=False)
            new_job.posted_by = request.user
            new_job.company = company
            new_job.save()
            print('tata nayan')

            # Add the selected disability types to the job
            new_job.disability_types.set(distypes)
            return redirect('post_job', user_id=request.user.id)  # Replace 'your_redirect_url' with the appropriate URL
        else:
            print("Form errors:", form.errors)
    else:
        form = JobForm()

    disability_types = DisabilityType.objects.all()
    template_name = 'contributors/post_jobs.html'
    context = {
        'form': form,
        'disability_types': disability_types,
        'categories_choices': Job.categories_choices,
        'job_type_choices': Job.job_type_choices,
        'mode_choices': Job.mode_choices,
        'time_choices': Job.time_choices,
        'companies': Companies.objects.filter(user=request.user).first(),
    }

    return render(request, template_name, context)


@login_required
def add_company(request, user_id):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('post_job', user_id=request.user.id)
        else:
            print("Form errors:", form.errors)
    else:
        form = CompanyForm()

    return render(request, 'contributors/add_company.html', {'form': form})


@login_required
def job_desktop(request, user_id):
    jobs_with_applicants_count = Job.objects.filter(posted_by=request.user).annotate(
        num_applicants=Count('applicant')
    )
    context = {
        'jobs_with_applicants_count': jobs_with_applicants_count,
    }
    template_name='contributors/JobsDesktop.html'
    return render(request, template_name, context)


def job_detail(request, job_id, user_id):
    job = get_object_or_404(Job, pk=job_id)
    applicants = Applicant.objects.filter(job=job)
    context = {
        'job': job,
        'applicants': applicants,
    }
    return render(request, 'contributors/job_details.html', context)
