from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.workplace}"


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_nr = models.CharField(max_length=100)
    contact_allowed = models.BooleanField(default=True)
    role = models.CharField(max_length=100)

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.workplace}"


class JobListing(models.Model):

    LOCATION_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
    ) 

    CATEGORY_CHOICES =( 
        ("1", "One"), 
        ("2", "Two"), 
        ("3", "Three"), 
        ("4", "Four"), 
        ("5", "Five"), 
    )

    WORK_TYPE_CHOICES =( 
        ("Full time", "Full time"), 
        ("Part time", "Part time"), 
        ("Summer job", "Summer job"), 
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(default="")

    work_type = models.CharField(choices=WORK_TYPE_CHOICES)
    location = models.CharField(choices=LOCATION_CHOICES)
    category = models.CharField(choices=CATEGORY_CHOICES)

    due_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.title} - {self.due_date}"


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField(default="")
    applied = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100)

    work_experiences = models.ManyToManyField(WorkExperience, blank=True)
    recommendations = models.ManyToManyField(Recommendation, blank=True)

    job_listing = models.ForeignKey(
        JobListing, on_delete=models.DO_NOTHING, default=None
    )

    def __str__(self, *args, **kwargs):
        return f"{self.user.username} - {self.status}"
