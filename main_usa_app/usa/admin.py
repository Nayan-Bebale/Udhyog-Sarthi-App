from django.contrib import admin
from .models import Job, JobSeeker, Contributor, SaveJobs, DisabilityType, Courses, Lecture, Blogs, Applicant, Companies

# Register your models here.

admin.site.register(Job)
admin.site.register(JobSeeker)
admin.site.register(Contributor)
admin.site.register(SaveJobs)
admin.site.register(DisabilityType)
admin.site.register(Courses)
admin.site.register(Lecture)
admin.site.register(Blogs)
admin.site.register(Applicant)
admin.site.register(Companies)