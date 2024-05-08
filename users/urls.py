from django.urls import path

from .views import SignInView, ProfileView

from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='users/sign-out.html'), name='sign-out'),
    path('profile/', ProfileView.as_view(), name='profile')
]
