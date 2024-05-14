from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from .models import JobListing
from django.shortcuts import HttpResponse, redirect

from is_ajax import is_ajax

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