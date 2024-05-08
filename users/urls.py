from django.urls import path

from .views import LoginView


urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("login/", LoginView.as_view(), name="login"),
]
