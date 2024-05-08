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

            #return redirect('/')
            return HttpResponse(json.dumps({'message': '200'}))
        else:
            if is_ajax(request=request):
                print(form.error_messages)
                print(form.error_messages['invalid_login'])
                #print(form.error_messages[0][0])
                print("AJAX")
        #return JsonResponse({"msg":'response3'}, status=200)
        #return redirect('login')
        return HttpResponse(json.dumps({'message': "Incorrect username or password. Try again."}))

class ProfileView(View):

    def get(self, request):
        if is_ajax(request=request):
            print(f"working2")

        context = {}
        return render(request, "users/profile.html", context)

    def post(self, request, name):
        # filter = FilterModel.objects.filter(name=name)
        # filter.delete()

        return JsonResponse({"result": "ok"}, status=200)
