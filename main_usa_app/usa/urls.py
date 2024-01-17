from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post-job/', views.post_job, name="post_job"),

    # login Registration system 
    path('login/', views.login, name="login"),
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
    path('courses/', views.courses, name="courses"),

    #blog And Post Url
    path('blogs/', views.blogs, name="blogs"),
    path('post-blogs/', views.post_blog, name="post_blog"),
    path('blog-detai/<int:blogid>/', views.blog_post_detail_page, name="blog_post_detail_page"),

    # JobSeeker Profile
    path('profile/', views.profile, name="profile"),
    path('edit-jobseeker-profile/', views.edit_jobseeker_profile, name="edit_jobseeker_profile"),

    # Countributor Profile
    path('contributor/', views.contributor, name="contributor"),
    path('edit-contributor-profile/', views.edit_contributor_profile, name="edit_contributor_profile"),
    path('blog_post_list_view/', views.blog_post_list_view, name="blog_post_list_view"),


    # All About Jobs
    path('jobseeker-jobs/', views.jobseeker_jobs, name="jobseeker_jobs"),

    path('list-saved-jobs/', views.list_save_job, name="list_save_job"),
    path('saved-jorb/<str:job_id>', views.save_job, name="save_job"),
    path('delete-saved-jorb/<str:job_id>', views.delete_save_job, name="delete_save_job"),

    # Blog by catogory
    path('disable-blog/<str:categories>', views.blog_by_type, name="blog_by_type"),
    path('main_dis_type/<str:name>', views.main_dis_type, name="main_dis_type"),

    # Create Course with Lectures
    path('create-course-with-lectures/', views.create_course_with_lectures, name="create_course_with_lectures"),
]