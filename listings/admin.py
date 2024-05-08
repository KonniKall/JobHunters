from django.contrib import admin

# Register your models here.

from .models import WorkExperience, Recommendation, Application, JobListing

admin.site.register(WorkExperience)
admin.site.register(Recommendation)
admin.site.register(Application)
admin.site.register(JobListing)
