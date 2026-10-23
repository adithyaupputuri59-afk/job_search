from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "company", "location", "salary")
    search_fields = ("title", "company", "location")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "applicant", "job", "applied_at", "status")
    list_filter = ("status", "applied_at")
    search_fields = ("applicant__username", "job__title")