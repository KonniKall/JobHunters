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

    title = forms.CharField(required=True, help_text="20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget= forms.TextInput(attrs={'v-on:change':'isTitle()', 'v-model':'title'}))
    #, '@keypress':'isEmail()'

    #work_type = forms.CharField(max_length=20, 
    #    widget= forms.TextInput(attrs={'@keypress':'isWorkType()', 'v-on:change':'isWorkType()', 'v-model':'workType'}))
        #@keypress="isNumber($event)"

    #due_date = forms.DateField(
    #    widget= forms.DateInput(attrs={'@keypress':'isDate()', 'v-on:change':'isDate()', 'v-model':'due_date'}))

    #due_date = forms.DateField(widget=DateInput)
    
    #start_date = forms.DateField(
    #    widget= forms.DateInput(attrs={'@keypress':'isDate()', 'v-on:change':'isDate()', 'v-model':'start_date'}))

    #start_date = forms.DateField(widget=DateInput)

    class Meta:
        model = JobListing
        fields = ['title', 'work_type', 'location', 'category']#, 'due_date', 'start_date']

class ContactInfoForm(ModelForm):
    #full_name = forms.CharField(
    #    widget= forms.TextInput(attrs={'v-model':'full_name'}))
    class Meta:
        model = ContactInfo
        fields = ['full_name', 'address', 'country', 'city', 'zip_code']

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'work_experiences', 'recommendations']

class ExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['workplace', 'role', 'start_date', 'end_date']

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ['name', 'email', 'phone_nr', 'role', 'contact_allowed']