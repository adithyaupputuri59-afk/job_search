from django.urls import path
from . import views

urlpatterns = [
    path("jobs/", views.job_list, name="job-list"),
    path("jobs/<int:pk>/", views.job_list, name="job-detail"),
    path("jobs/delete-all/", views.delete_all_jobs, name="delete-all-jobs"),
    path("jobs/upload-excel/", views.upload_excel, name="upload-excel"),
    path("jobs/sample-excel/", views.download_sample_excel, name="sample-excel"),
    path("jobs/download-sample-excel/", views.download_sample_excel, name="download-sample-excel"),
    path("applications/",views.application_list,name="application-list"),
]

