from django.contrib import admin

# Register your models here.

from .models import Work_Experience, Reccomendation, Application
    
admin.site.register(Work_Experience)
admin.site.register(Reccomendation)
admin.site.register(Application)