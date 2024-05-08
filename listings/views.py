from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from .models import JobListing
from django.shortcuts import HttpResponse

from ..is_ajax import is_ajax

# Create your views here.


class ListingsView(View):

    def get(self, request):
        # listings = list(JobListing.objects.filter(user=request.user).values())
        # listings = list(JobListing.objects.all)

        if is_ajax(request=request):
            print(f"working2")
            # return JsonResponse({'listings': listings}, status=200)
        context = {}
        return render(request, "listings/job_listings.html", context)

    def post(self, request, name):
        # filter = FilterModel.objects.filter(name=name)
        # filter.delete()

        return JsonResponse({"result": "ok"}, status=200)

"""class MockDataView(View):
    def post(self, request, x):
        blabalb ef x er y
        JL = JobListing(user=self.user, )
        JL.save()"""