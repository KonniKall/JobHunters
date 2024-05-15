from django.urls import path

from .views import ListingsView, JobListingView, CreateJobListingView, JobListingApplicationView, ApplicationContactView, ApplicationExperiencesView

from django.conf.urls import handler404

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path('', ListingsView.as_view(), name='index'),
    path('listing/<str:listing>/', JobListingView.as_view(), name='listing'),

    path('create/job-listing/', CreateJobListingView.as_view(), name='create-job-listing'),
    path('apply/<str:listing>/', JobListingApplicationView.as_view(), name='job-listing-application'),
    path('application/contact/', ApplicationContactView.as_view(), name='application-contact'),
    path('application/contact/<str:full_name>/<str:address>/<str:country>/<str:city>/<str:zip_code>/', ApplicationContactView.as_view(), name='application-contact'),
    #path('application/contact/', ApplicationContactView.as_view(), name='application-contact'),
    path('application/experiences/', ApplicationExperiencesView.as_view(), name='application-contact'),
]