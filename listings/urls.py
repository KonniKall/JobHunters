from django.urls import path

from .views import ListingsView, JobListingView

from django.conf.urls import handler404

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path('', ListingsView.as_view(), name='index'),
    path('listing/<str:listing>/', JobListingView.as_view(), name='listing')
]