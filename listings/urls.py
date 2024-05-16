from django.urls import path

from .views import ListingsView, JobListingView, CreateJobListingView, JobListingApplicationView, ApplicationContactView, ApplicationExperiencesView, ApplicationRecommendationsView, ApplicationView, FilterView

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
    path('application/experiences/', ApplicationExperiencesView.as_view(), name='application-experience'),
    path('add/experience/<str:workplace>/<str:role>/<str:start_date>/<str:end_date>/', ApplicationExperiencesView.as_view(), name='application-experience-add'),
    path('delete/experience/<str:experience>/', ApplicationExperiencesView.as_view(), name='application-experience'),
    
    path('application/recommendations/', ApplicationRecommendationsView.as_view(), name='application-recommendations'),
    path('add/recommendation/<str:name>/<str:email>/<str:phone>/<str:role>/<str:contact_allowed>/', ApplicationRecommendationsView.as_view(), name='application-recommendation-add'),
    path('delete/recommendation/<str:recommendation>/', ApplicationRecommendationsView.as_view(), name='application-recommendation'),

    path('add/application/<str:listing>/<str:cover_letter>/', ApplicationView.as_view(), name='submit-application'),

    path('filter/<str:job_name>/<str:company_name>/<str:order>/<str:category>/<str:applied>/', FilterView.as_view(), name='filter'),
]