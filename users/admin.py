from django.contrib import admin

# Register your models here.

from .models import Profile, Contact_Info, Employer, Job_Seeker
    
admin.site.register(Profile)
admin.site.register(Contact_Info)
admin.site.register(Employer)
admin.site.register(Job_Seeker)