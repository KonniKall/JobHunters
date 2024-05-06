from django.contrib import admin

# Register your models here.

from .models import WorkExperience, Reccomendation, Application
    
admin.site.register(WorkExperience)
admin.site.register(Reccomendation)
admin.site.register(Application)