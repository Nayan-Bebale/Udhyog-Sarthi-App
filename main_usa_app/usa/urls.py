from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('post-job/', views.post_job, name="post_job"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),


    path('property-list/', views.property_list, name="property_list"),
    path('property-agent/', views.property_agent, name="property_agent"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('property-type/', views.property_type, name="property_type"),
    path('property-type/<str:job_type>', views.job_list_by_type, name="job_list_by_type"),

    path('contact/', views.contect, name="contect"),
    path('about/', views.about, name="about"),
    path('blogs/', views.blogs, name="blogs"),


    path('profile/', views.profile, name="profile"),
    path('contributor/', views.contributor, name="contributor"),


    path('jobseeker-jobs/', views.jobseeker_jobs, name="jobseeker_jobs"),

]