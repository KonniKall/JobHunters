from django.urls import path

from .views import ListingsView


urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path('', ListingsView.as_view()),
    
]