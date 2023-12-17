from django.contrib import admin
from .models import Job, JobSeeker, Contributor, SaveJobs

# Register your models here.

admin.site.register(Job)
admin.site.register(JobSeeker)
admin.site.register(Contributor)
admin.site.register(SaveJobs)