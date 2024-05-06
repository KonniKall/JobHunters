from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class ListingsView(View):
    def get(self, request):
        context = {
            #'posts': Post.objects.all()
    
        }
        return render(request, 'listings/job_listings.html', context)
    
    def post(self, request, name):
        #filter = FilterModel.objects.filter(name=name)
        #filter.delete()

        return JsonResponse({'result': 'ok'}, status=200)