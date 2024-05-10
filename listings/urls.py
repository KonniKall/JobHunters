from django.urls import path

from .views import ListingsView

from django.conf.urls import handler404

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path('', ListingsView.as_view(), name='index')
    
]