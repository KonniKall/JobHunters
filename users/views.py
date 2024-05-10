from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse


from is_ajax import is_ajax

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .forms import UserSignInForm#, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponse

import json

from listings.models import Application, JobListing
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
        applications = Application.objects.filter(user=request.user)
        context = {'applications': applications}
        return render(request, "users/applications.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)
    
class ApplicationView(View):

    def get(self, request, application):
        #Nota mögulega ehv annað en pk seinna
        application = Application.objects.filter(user=request.user, pk=application).first()
        if application == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        context = {'application': application}
        return render(request, "users/application.html", context)

    def post(self, request, name):

        return JsonResponse({"result": "ok"}, status=200)


def custom_page_not_found_view(request, exception=None):

    return render(request, "listings/404.html")