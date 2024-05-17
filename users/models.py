from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

COUNTRY_CHOICES = (
    ("Iceland", "Iceland"),
    ("Denmark", "Denmark"),
    ("England", "England"),
    ("United States", "United States"),
    ("Bolivia", "Bolivia"),
)


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_nr = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(choices=COUNTRY_CHOICES)
    zip_code = models.CharField(max_length=100)

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.address}"


class JobSeeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(default="", blank=True)

    def __str__(self, *args, **kwargs):
        return f"JobSeeker"


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")
    address = models.CharField(max_length=100)

    cover_img = models.ImageField(default="default_cover.png")

    def __str__(self, *args, **kwargs):
        return f"Employer"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default="default_profile_img.png")

    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.email}"
