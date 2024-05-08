from django.urls import path

from .views import SignInView, ProfileView


urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path('profile/', ProfileView.as_view(), name='profile')
]
