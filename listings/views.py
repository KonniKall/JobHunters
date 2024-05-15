from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from .models import JobListing
from django.shortcuts import HttpResponse, redirect

from is_ajax import is_ajax

from .forms import JobListingCreationForm

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
        if listing == None:
            # Appendar við URL-in sem þarf að laga
            return redirect('/users.views.custom_page_not_found_view')
        context = {'listing': listing}
        return render(request, "listings/job_listing.html", context)
    

class CreateJobListingView(View):

    def get(self, request):
        context = {}
        context['form'] = JobListingCreationForm()
        return render(request, "listings/create-job-listing.html", context)

    def post(self, request):
        form = JobListingCreationForm(data=request.POST)
        #start_date = form('start_date')
        start_date = request.POST['start_date']
        print(start_date)
        if form.is_valid():
            print('working?')
            instance = form.save(commit=False)
            instance.user = request.user
            start_date = datetime.datetime.strptime(request.POST['start_date'], "%m/%d/%Y").date()
            instance.start_date = start_date
            due_date = datetime.datetime.strptime(request.POST['due_date'], "%m/%d/%Y").date()
            instance.due_date = due_date
            instance.save()

        return redirect('my-job-listings')
