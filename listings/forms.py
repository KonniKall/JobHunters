from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django.forms import fields, ModelForm
from .models import JobListing, Application, WorkExperience, Recommendation
from users.models import ContactInfo

#from crispy_forms.helper import FormHelper

class DateInput(forms.DateInput):
    input_type = 'date'

class JobListingCreationForm(ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'work_type', 'location', 'category']#, 'due_date', 'start_date']

class ContactInfoForm(ModelForm):
    #full_name = forms.CharField(
    #    widget= forms.TextInput(attrs={'v-model':'full_name'}))
    class Meta:
        model = ContactInfo
        fields = ['full_name', 'address', 'country', 'city', 'zip_code']

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['contact_information', 'cover_letter', 'work_experiences', 'recommendations']

class ExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['workplace', 'role', 'start_date', 'end_date']

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ['name', 'email', 'phone_nr', 'role', 'contact_allowed']