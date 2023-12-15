from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
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
    id_user = models.AutoField(primary_key=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-pic.png')
    location = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    udid = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    about = models.CharField(max_length=500, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    dis_type = models.CharField(max_length=30)


    def __str__(self):
        return self.user.username

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-pic.png')

    def __str__(self):
        return self.user.username
