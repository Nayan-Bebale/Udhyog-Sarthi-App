from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type_choices = [
        ('marketing', 'Marketing'),
        ('design', 'Design'),
        ('development', 'Development'),
        ('customer', 'Customer'),
        ('health_caare', 'Health and Caare'),
        ('automotive', 'Automotive jobs'),
        ('data_entry', 'Data entry'),
        ('call_center', 'Call center'),
    ]
    job_type = models.CharField(max_length=20, choices=job_type_choices)
    mode_choices = [
        ('hibrid', 'Hibrid'),
        ('remote', 'Remote'),
        ('wfo', 'WFO')
    ]
    mode = models.CharField(max_length=10, choices=mode_choices)
    time_choices = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
    ]
    time = models.CharField(max_length=10, choices=time_choices)
    categories_choices = [
        ('government', 'Government'),
        ('private', 'Private'),
    ]
    categories = models.CharField(max_length=10, choices=categories_choices)
    disability_types = models.ManyToManyField('DisabilityType', related_name='jobs', blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hours = models.PositiveIntegerField()
    about = models.TextField()
    day_ago = models.PositiveIntegerField()
    image = models.ImageField(upload_to='job_images/', default='D:\main_usa_app\main_usa_app\main_usa_app\media\default_job_banner.jpg')
    posted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)



    def __str__(self):
        return self.job_title
    


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(max_length=30)
    id_user = models.AutoField(primary_key=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images/', default='blank-profile-pic.png')
    location = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    udid = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    about = models.CharField(max_length=500, blank=True)

    dis_type = models.CharField(max_length=30)
    

    def __str__(self):
        return self.user.username

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-pic.png')

    def __str__(self):
        return self.user.username


class SaveJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} saved {self.job.job_title}"



# Course Model
    
class DisabilityType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    job_opportunities = models.ManyToManyField(Job, blank=True)
    

    def __str__(self):
        return self.name
    


    
class Courses(models.Model):

    # Unique identifier for the course
    course_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255)
    description = RichTextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courseimg = models.ImageField(upload_to='courses_images/', default='default_course.jpg')

    
    disability_types = models.ManyToManyField('DisabilityType', related_name='courses', blank=True)

    def __str__(self):
        return self.title



class Lecture(models.Model):
    # Foreign key referencing the Course model
    course = models.ForeignKey(Courses, related_name='lectures', on_delete=models.CASCADE)
    
    # Lecture Information
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = RichTextField()
    sequence_order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.title} - Lecture {self.sequence_order}: {self.title}"


class Blogs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    id_blog = models.AutoField(primary_key=True)
    abstraction = models.TextField(max_length=250, blank=True)
    disability_types = models.ManyToManyField('DisabilityType', related_name='blogs', blank=True)

    content = RichTextField()
    tumbnail = models.ImageField(upload_to='blogs_images/', default='default_blogs.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
