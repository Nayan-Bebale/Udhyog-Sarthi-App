from django.urls import path
from . import views
from searches.views import search_view

app_name = 'usa'

urlpatterns = [
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
    path('blogs/<int:year>/<int:month>/', views.blog_month, name='blog_month'),
    path('blog-detail/<int:blogid>/', views.blog_post_detail_page, name="blog_post_detail_page"),

    # Blog by catogory
    path('disable-blog/<str:categories>', views.blog_by_type, name="blog_by_type"),
    path('main_dis_type/<str:name>', views.main_dis_type, name="main_dis_type"),

    path('chat/', views.chatoption, name='chatoption'),

    # Create Course with Lectures
    path('create-course-with-lectures/', views.create_course_with_lectures, name="create_course_with_lectures"),
]