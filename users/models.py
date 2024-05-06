from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contact_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.address}'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_nr = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_img = models.ImageField(default='default_user.png')
    

    time_posted = models.DateTimeField(default=timezone.now)
    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.email}'