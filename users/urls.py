from django.urls import path

from .views import LoginView, ProfileView


urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("login/", LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name='profile')
]
