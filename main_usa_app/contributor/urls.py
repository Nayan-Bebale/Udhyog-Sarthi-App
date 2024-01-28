from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_id>/', views.contributor, name="contributor"),
    path('<int:user_id>/edit-contributor-profile/', views.edit_contributor_profile, name="edit_contributor_profile"),
    path('<int:user_id>/blog_post_list_view/', views.blog_post_list_view, name="blog_post_list_view"),
    path('<int:user_id>/post-blogs/', views.post_blog, name="post_blog"),
    path('<int:user_id>/post-job/', views.post_job, name="post_job"),
    path('<int:user_id>/post-company/', views.add_company, name="add_company"),
    path('<int:user_id>/job_desktop/', views.job_desktop, name="job_desktop"),
    path('<int:user_id>/job_detail/<str:job_id>/', views.job_detail, name="job_detail"),
]
