from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.workplace}'
    
class Reccomendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_nr = models.CharField(max_length=100)
    contact_allowed = models.BooleanField(default=True)
    role = models.CharField(max_length=100)

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.workplace}'
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField(default='')
    applied = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100)

    work_experiences = models.ManyToManyField(WorkExperience)
    reccomendations = models.ManyToManyField(Reccomendation)

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.status}'

    #def __str__(self, *args, **kwargs):
    #    return f'{self.user.username} Profile'