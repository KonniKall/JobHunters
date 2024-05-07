from django.contrib import admin

# Register your models here.

from .models import WorkExperience, Reccomendation, Application, JobListing
    
admin.site.register(WorkExperience)
admin.site.register(Reccomendation)
admin.site.register(Application)
admin.site.register(JobListing)