from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('post-job/', views.post_job, name="post_job"),


    path('property-list/', views.property_list, name="property_list"),
    path('property-agent/', views.property_agent, name="property_agent"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('property-type/', views.property_type, name="property_type"),

    path('contact/', views.contect, name="contect"),
    path('about/', views.about, name="about"),
]