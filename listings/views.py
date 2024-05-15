from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from .models import JobListing, Application, Recommendation, WorkExperience
from django.shortcuts import HttpResponse, redirect
from users.models import Employer

from is_ajax import is_ajax

from .forms import JobListingCreationForm, ContactInfoForm, ApplicationForm, ExperienceForm

import datetime

# Create your views here.


class ListingsView(View):

    def get(self, request):
        # listings = list(JobListing.objects.filter(user=request.user).values())
        listings = JobListing.objects.all()

        # if is_ajax(request=request):
        #     print(f"working2")
        #     return JsonResponse({"listings": listings}, status=200)
        #     # return {"listings": listings}
        context = {"listings": listings}
        return render(request, "listings/job_listings.html", context)

    def post(self, request, name):
        # filter = FilterModel.objects.filter(name=name)
        # filter.delete()

        return JsonResponse({"result": "ok"}, status=200)


class JobListingView(View):
    def get(self, request, listing):
        listing = JobListing.objects.filter(pk=listing).first()
        company = Employer.objects.filter(user=listing.user).first()
        company_listings = JobListing.objects.filter(user=listing.user)
        if listing == None:
            # Appendar við URL-in sem þarf að laga
            return redirect("/users.views.custom_page_not_found_view")
        context = {
            "listing": listing,
            "company": company,
            "company_listings": company_listings,
        }
        return render(request, "listings/job_listing.html", context)


class CreateJobListingView(View):

    def get(self, request):
        context = {}
        context["form"] = JobListingCreationForm()
        return render(request, "listings/create-job-listing.html", context)

    def post(self, request):
        form = JobListingCreationForm(data=request.POST)
        # start_date = form('start_date')
        start_date = request.POST["start_date"]
        print(start_date)
        if form.is_valid():
            print("working?")
            instance = form.save(commit=False)
            instance.user = request.user
            start_date = datetime.datetime.strptime(
                request.POST["start_date"], "%m/%d/%Y"
            ).date()
            instance.start_date = start_date
            due_date = datetime.datetime.strptime(
                request.POST["due_date"], "%m/%d/%Y"
            ).date()
            instance.due_date = due_date
            instance.save()

        return redirect('my-job-listings')
    
from users.models import ContactInfo

class JobListingApplicationView(View):
    def get(self, request, listing):
        listing = JobListing.objects.filter(pk=listing).first()
        if listing == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        contact_info = ContactInfo.objects.filter(user=request.user).first()
        work_experiences = WorkExperience.objects.filter(user=request.user)
        recommendations = Recommendation.objects.filter(user=request.user)

        COUNTRY_CHOICES = [
        {"country": "Iceland"}, 
        {"country": "Denmark"}, 
        {"country": "England"}, 
        {"country": "United States"}, 
        {"country": "Bolivia"}, 
        ]

        context = {
            'listing': listing,
            'contact_info': contact_info,
            'work_experiences': work_experiences,
            'recommendations': recommendations,
            'country_choices': COUNTRY_CHOICES
        }
        context['application_form'] = ApplicationForm()
        #context['contact_form'] = ContactInfoForm(initial={'full_name': contact_info.full_name, 'address': contact_info.address, 'country': contact_info.country, 'city': contact_info.city, 'zip_code': contact_info.zip_code})
        context['experience_form'] = ExperienceForm()
        return render(request, "listings/job_listing_application.html", context)
    
    def post(self, request, listing):
        form = ExperienceForm(data=request.POST)
        context = {}
        return JsonResponse({"error": "Not AJAX request."})
    

class ApplicationContactView(View):
    def get(self, request):
        contact = list(ContactInfo.objects.filter(user=request.user).values())
        #application = list(FilterModel.objects.filter(user=request.user).exclude(name='Unsaved').values())
        context = {'contact': contact}
        return JsonResponse(context, status=200)
    
    def post(self, request, full_name, address, country, city, zip_code):
        form = ContactInfoForm(data={
            'full_name': full_name, 'address': address, 'country': country,
            'city': city, 'zip_code': zip_code
        })

        """print(form.is_valid())
        for field in form:
            print("Field Error:", field.name,  field.errors)"""
        
        if is_ajax(request=request) and form.is_valid():

            obj, created = ContactInfo.objects.filter(user=request.user).update_or_create(
                user=request.user,
                defaults={'user': request.user, 'full_name': full_name, 'address': address, 'country': country, 'city': city, 'zip_code': zip_code},
                create_defaults={'user': request.user, 'full_name': full_name, 'address': address, 'country': country, 'city': city, 'zip_code': zip_code})
            try: obj.save()
            except: created.save()
            print(obj.zip_code)
        return JsonResponse({"error": "Not AJAX request."})
    
class ApplicationExperiencesView(View):
    def get(self, request):
        experiences = list(WorkExperience.objects.filter(user=request.user).values())
        #application = list(FilterModel.objects.filter(user=request.user).exclude(name='Unsaved').values())
        context = {'experiences': experiences}
        return JsonResponse(context, status=200)
    def post(self, request, experiences):
        for experience in experiences:
            form = ExperienceForm(data={
                
            })

            if is_ajax(request=request) and form.is_valid():
                
                """obj, created = ContactInfo.objects.filter(user=request.user).update_or_create(
                    user=request.user,
                    defaults={'user': request.user, 'full_name': full_name, 'address': address, 'country': country, 'city': city, 'zip_code': zip_code},
                    create_defaults={'user': request.user, 'full_name': full_name, 'address': address, 'country': country, 'city': city, 'zip_code': zip_code})
                try: obj.save()
                except: created.save()
                print(obj.zip_code)"""
        return JsonResponse({"error": "Not AJAX request."})
    
