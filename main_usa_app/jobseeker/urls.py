from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_id>/profile/', views.profile, name="profile"),
    path('<int:user_id>/user-profile/', views.user_profile, name="user_profile"),
    path('<int:user_id>/edit-jobseeker-profile/', views.edit_jobseeker_profile, name="edit_jobseeker_profile"),
    path('<int:user_id>/jobseeker-jobs/', views.jobseeker_jobs, name="jobseeker_jobs"),
    path('<int:user_id>/list-saved-jobs/', views.list_save_job, name="list_save_job"),
    path('<int:user_id>/saved-jorb/<str:job_id>/', views.save_job, name="save_job"),
    path('<int:user_id>/delete-saved-jorb/<str:job_id>/', views.delete_save_job, name="delete_save_job"),
    path('<int:user_id>/show-details-jobs/<str:job_id>/', views.show_details_jobs, name="show_details_jobs"),
    path('<int:user_id>/blogs/', views.blogs_jobseekers, name="blogs_jobseekers"),
    path('<int:user_id>/blogs/blog-detail/<int:blogid>/', views.blog_details_jobseeker, name="blog_details_jobseeker"),
    path('<int:user_id>/blogs/<int:year>/<int:month>/', views.blog_by_month, name='blog_by_month'),
    path('<int:user_id>/disable-blog/<str:categories>', views.blog_by_type_jobseeker, name="blog_by_type_jobseeker"),
    path('<int:user_id>/main_dis_type/<str:name>', views.main_dis_type_jobseeker, name="main_dis_type_jobseeker"),
]

