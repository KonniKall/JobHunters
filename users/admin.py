from django.contrib import admin

# Register your models here.

from .models import Profile, ContactInfo, Employer, JobSeeker
    
admin.site.register(Profile)
admin.site.register(ContactInfo)
admin.site.register(Employer)
admin.site.register(JobSeeker)