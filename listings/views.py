from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from .models import JobListing, Application, Recommendation, WorkExperience
from django.shortcuts import HttpResponse, redirect
from users.models import Employer

from is_ajax import is_ajax

from .forms import (
    JobListingCreationForm,
    ContactInfoForm,
    ApplicationForm,
    ExperienceForm,
    RecommendationForm,
)

import datetime

from users.models import JobSeeker
from django.contrib.auth.models import User

# Create your views here.


class ListingsView(View):

    def get(self, request):
        listings = JobListing.objects.all()

        context = {"listings": listings}
        return render(request, "listings/job_listings.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)


class JobListingView(View):
    def get(self, request, listing):
        listing = JobListing.objects.filter(pk=listing).first()
        company = Employer.objects.filter(user=listing.user).first()
        company_listings = JobListing.objects.filter(user=listing.user)
        applied = False

        if request.user.is_authenticated:
            if Application.objects.filter(user=request.user, job_listing=listing):
                applied = True
        if listing == None:
            # Appendar við URL-in sem þarf að laga
            return redirect("/users.views.custom_page_not_found_view")
        context = {
            "listing": listing,
            "company": company,
            "company_listings": company_listings,
            "applied": applied
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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            due_date = datetime.datetime.strptime(
                request.POST["due_date"], "%m/%d/%Y"
            ).date()
            instance.due_date = due_date
            instance.save()

        return redirect("my-job-listings")


from users.models import ContactInfo


class JobListingApplicationView(View):
    def get(self, request, listing):
        if request.user.is_authenticated:
            listing = JobListing.objects.filter(pk=listing).first()
            if listing == None:
                # Appendar við URL-in sem þarf að laga
                return redirect("/users.views.custom_page_not_found_view")
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
                "listing": listing,
                "contact_info": contact_info,
                "work_experiences": work_experiences,
                "recommendations": recommendations,
                "country_choices": COUNTRY_CHOICES,
            }
            context["application_form"] = ApplicationForm()
            # context['contact_form'] = ContactInfoForm(initial={'full_name': contact_info.full_name, 'address': contact_info.address, 'country': contact_info.country, 'city': contact_info.city, 'zip_code': contact_info.zip_code})
            context["experience_form"] = ExperienceForm()
            return render(request, "listings/job_listing_application.html", context)
        else:
            return redirect("index")

    def post(self, request, listing):
        form = ExperienceForm(data=request.POST)
        context = {}
        return JsonResponse({"error": "Not AJAX request."})


class ApplicationContactView(View):
    def get(self, request):
        contact = list(ContactInfo.objects.filter(user=request.user).values())
        # application = list(FilterModel.objects.filter(user=request.user).exclude(name='Unsaved').values())
        context = {"contact": contact}
        return JsonResponse(context, status=200)

    def post(self, request, full_name, address, country, city, zip_code):
        form = ContactInfoForm(
            data={
                "full_name": full_name,
                "address": address,
                "country": country,
                "city": city,
                "zip_code": zip_code,
            }
        )

        """print(form.is_valid())
        for field in form:
            print("Field Error:", field.name,  field.errors)"""

        if is_ajax(request=request) and form.is_valid():

            obj, created = ContactInfo.objects.filter(
                user=request.user
            ).update_or_create(
                user=request.user,
                defaults={
                    "user": request.user,
                    "full_name": full_name,
                    "address": address,
                    "country": country,
                    "city": city,
                    "zip_code": zip_code,
                },
                create_defaults={
                    "user": request.user,
                    "full_name": full_name,
                    "address": address,
                    "country": country,
                    "city": city,
                    "zip_code": zip_code,
                },
            )
            try:
                obj.save()
            except:
                created.save()
        return JsonResponse({"error": "Not AJAX request."})


class ApplicationExperiencesView(View):
    def get(self, request):
        experiences = list(WorkExperience.objects.filter(user=request.user).values())
        # application = list(FilterModel.objects.filter(user=request.user).exclude(name='Unsaved').values())
        context = {"experiences": experiences}
        return JsonResponse(context, status=200)

    def post(self, request, workplace, role, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, "%m-%d-%Y").date()
        end_date = datetime.datetime.strptime(end_date, "%m-%d-%Y").date()

        form = ExperienceForm(
            data={
                "workplace": workplace,
                "role": role,
                "start_date": start_date,
                "end_date": end_date,
            }
        )

        if is_ajax(request=request) and form.is_valid():
            obj = WorkExperience.objects.create(
                user=request.user,
                workplace=workplace,
                role=role,
                start_date=start_date,
                end_date=end_date,
            )
            obj.save()
            return JsonResponse({"response": "201"})

        return JsonResponse({"error": "Not AJAX request."})

    def delete(self, request, experience):
        experience = WorkExperience.objects.filter(user=request.user, pk=experience)
        experience.delete()
        return JsonResponse({"response": "deleted."})


class ApplicationRecommendationsView(View):
    def get(self, request):
        recommendations = list(
            Recommendation.objects.filter(user=request.user).values()
        )
        context = {"recommendations": recommendations}
        return JsonResponse(context, status=200)

    def post(self, request, name, email, phone, role, contact_allowed):

        if contact_allowed == "true":
            contact_allowed = True
        else:
            contact_allowed = False

        form = RecommendationForm(
            data={
                "name": name,
                "email": email,
                "phone_nr": phone,
                "role": role,
                "contact_allowed": contact_allowed,
            }
        )

        if is_ajax(request=request) and form.is_valid():
            obj = Recommendation.objects.create(
                user=request.user,
                name=name,
                email=email,
                phone_nr=phone,
                role=role,
                contact_allowed=contact_allowed,
            )
            obj.save()
            return JsonResponse({"response": "201"})

        return JsonResponse({"error": "Not AJAX request."})

    def delete(self, request, recommendation):
        experience = Recommendation.objects.filter(user=request.user, pk=recommendation)
        experience.delete()
        return JsonResponse({"response": "deleted."})


class ApplicationView(View):

    def get(self, request, application):
        # Job seeker check
        if JobSeeker.objects.filter(user=request.user).first() == None:
            return redirect("/users.views.custom_page_not_found_view")
        # Nota mögulega ehv annað en pk seinna
        application = Application.objects.filter(
            user=request.user, pk=application
        ).first()
        if application == None:
            # Appendar við URL-in sem þarf að laga
            return redirect("/users.views.custom_page_not_found_view")
        context = {"application": application}
        return render(request, "users/application.html", context)

    def post(self, request, listing, cover_letter):
        
        contact_information = ContactInfo.objects.filter(user=request.user).first()
        work_experiences = WorkExperience.objects.filter(user=request.user)
        recommendations = Recommendation.objects.filter(user=request.user)

        listing = JobListing.objects.filter(pk=listing).first()

        if Application.objects.filter(job_listing=listing, user=request.user):
            return JsonResponse({'Forbidden': 'You have already applied for this listing'}, status=403)

        form = ApplicationForm(
            data={
                "contact_information": contact_information,
                "cover_letter": cover_letter,
                "work_experiences": work_experiences,
                "recommendations": recommendations,
            }
        )

        if is_ajax(request=request) and form.is_valid():
            obj = Application.objects.create(
                user=request.user,
                contact_information=contact_information,
                job_listing=listing,
            )
            for experience in work_experiences:
                obj.work_experiences.add(experience)
            for recommendation in recommendations:
                obj.recommendations.add(recommendation)
            obj.save()

        return JsonResponse({"error": "Not AJAX request."})
        return JsonResponse({"result": "ok"}, status=200)
    

class FilterView(View):

    def get(self, request, job_name, company_name, order, category, applied):
        filter_dict = {}

        if job_name != 'none':
            filter_dict['title__icontains'] = job_name
        if company_name != 'none':
            #companies = User.objects.filter(username__icontains=company_name)
            filter_dict['user__username__icontains'] = company_name
        if category != 'all':
            filter_dict['category__icontains'] = category
        if filter_dict == {}:
            job_listings = JobListing.objects.all()
        else:
            job_listings = JobListing.objects.filter(**filter_dict)

        if order != 'none':
            job_listings = job_listings.order_by(order)

        #Check if user has applied for job before
        if applied == 'true': applied = True
        else: applied = False
        to_be_removed = []

        if request.user.is_authenticated:
            if applied:
                for job_listing in job_listings:
                    if not Application.objects.filter(user=request.user, job_listing=job_listing).exists():
                        to_be_removed.append(job_listing.id)
            else:
                for job_listing in job_listings:
                    if Application.objects.filter(user=request.user, job_listing=job_listing).exists():
                        to_be_removed.append(job_listing.id)

        job_listings = job_listings.exclude(id__in=to_be_removed)

        #Collects usernames of the users that posted the job listings
        user_list = {}
        for job_listing in job_listings:
            user_list[job_listing.user.pk] = job_listing.user.username

        #Takes the values from job listings so they can be served
        job_listings = list(job_listings.distinct().values())

        context = {
            "job_listings": job_listings,
            "user_list": user_list
        }

        if is_ajax(request=request):
            return JsonResponse(context, status=200)
        
        return render(request, "listings/job_listings.html", context)
