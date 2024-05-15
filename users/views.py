from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse


from is_ajax import is_ajax

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .forms import UserSignInForm #, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponse

import json

from listings.models import Application, JobListing
from .models import Employer, JobSeeker
from django.contrib.auth.models import User

from django.shortcuts import redirect

# Create your views here.


class SignInView(View):

    def get(self, request):
        # listings = list(JobListing.objects.filter(user=request.user).values())
        # listings = list(JobListing.objects.all)

        if is_ajax(request=request):
            print(f"working2")
            # return JsonResponse({'listings': listings}, status=200)
        context = {}
        return render(request, "users/sign-in.html", context)

    def post(self, request):
        form = UserSignInForm(data=request.POST)
        if form.is_valid():
            print('working?')
            usernameS = form.cleaned_data.get('username')
            passwordS = form.cleaned_data.get('password')
            messages.success(request, f'Signed in as {usernameS}.')
            user = authenticate(username=usernameS, password=passwordS)
            auth_login(request, user)
            print('authenticated')
            if is_ajax(request=request):
                print("AJAX2")

            return HttpResponse(json.dumps({'message': '200'}))
        else:
            if is_ajax(request=request):
                print(form.error_messages)
                print(form.error_messages['invalid_login'])
                print("AJAX")

        return HttpResponse(json.dumps({'message': "Incorrect username or password. Try again."}))

class ProfileView(View):

    def get(self, request):
        if is_ajax(request=request):
            print(f"working2")

        context = {}
        return render(request, "users/profile.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)


class ApplicationsView(View):

    def get(self, request):
        #Job seeker check
        if JobSeeker.objects.filter(user=request.user).first() == None:
            return redirect('/users.views.custom_page_not_found_view')
        applications = Application.objects.filter(user=request.user)
        context = {'applications': applications}
        return render(request, "users/applications.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    
class ApplicationView(View):

    def get(self, request, application):
        #Job seeker check
        if JobSeeker.objects.filter(user=request.user).first() == None:
            return redirect('/users.views.custom_page_not_found_view')
        #Nota mögulega ehv annað en pk seinna
        application = Application.objects.filter(user=request.user, pk=application).first()
        if application == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        context = {'application': application}
        return render(request, "users/application.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)


class JobListingsView(View):

    def get(self, request):
        #Employer check
        if Employer.objects.filter(user=request.user).first() == None:
            return redirect('/users.views.custom_page_not_found_view')
        
        job_listings = JobListing.objects.filter(user=request.user)
        context = {'job_listings': job_listings}
        return render(request, "users/job-listings.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    
class JobListingView(View):

    def get(self, request, job_listing):
        #Employer check
        if Employer.objects.filter(user=request.user).first() == None:
            return redirect('/users.views.custom_page_not_found_view')

        #Nota mögulega ehv annað en pk seinna
        job_listing = JobListing.objects.filter(user=request.user, pk=job_listing).first()
        if job_listing == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        context = {'job_listing': job_listing}
        return render(request, "users/job-listing.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    
class WorkplacesView(View):

    def get(self, request):
        workplaces = Employer.objects.all()
        context = {'workplaces': workplaces}
        return render(request, "users/workplaces.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    
class WorkplaceView(View):

    def get(self, request, workplace):
        workplace = Employer.objects.filter(user=request.user, pk=workplace).first()
        if workplace == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        context = {'workplace': workplace}
        return render(request, "users/workplace.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    



def custom_page_not_found_view(request, exception=None):

    return render(request, "listings/404.html")


